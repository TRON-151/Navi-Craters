from libraries import *
from timer_lib import Timer
from os.path import join
      
class Player(pygame.sprite.Sprite):
   def __init__(self, position, groups, collision_sprites):
      super().__init__(groups)

      self.image = pygame.image.load(join('graphics','astronaut','idle','01.png')) 
      self.z = Z_axis['Terrain']
      #player rect
      self.rect = self.image.get_frect(topleft = position)
      self.hitbox_rect = self.rect.inflate(-6, -6)
      self.old_rect = self.hitbox_rect.copy()

      #movement
      self.direction = vector()
      self.speed = 100
      self.gravity = 250
      self.jump = False
      #jump setting
      self.jump_height = 170

      #collision
      self.collision_sprites = collision_sprites
      #touching surface
      self.on_surface = {'floor': False, 'left': False, 'right': False, 'ceiling': False }


      #timer
      self.timers = {
         'wall_jump': Timer(500),
         'wall_slide_block': Timer(250)
      }

      #sound effect
      self.jump_effect = pygame.mixer.Sound(join("audio","jump.mp3"))
      self.jump_effect.set_volume(0.3)

      #testing contact rect
      # self.display_surface = pygame.display.get_surface()


   def input(self):
      keys = pygame.key.get_pressed()

      input_vector = vector(0,0)
      
      if not self.timers['wall_jump'].active:       
         # right movement key---------> 
         if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            input_vector.x += 1
         # left movement key<---------
         if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            input_vector.x -= 1

         self.direction.x = input_vector.normalize().x if input_vector else 0
      #jump
      if keys[pygame.K_SPACE]:
         
         self.jump = True
      

   def move(self,delta_time):
      #horizontal movement
      self.hitbox_rect.x += self.direction.x * self.speed * delta_time
      self.collision('horizontal')


      #vertical movement
      if not self.on_surface['floor'] and any((self.on_surface['left'], self.on_surface['right'])) and not self.timers['wall_slide_block'].active:
         self.direction.y += 0
         self.hitbox_rect.y += self.gravity/10 * delta_time 
      else:
         self.direction.y += self.gravity / 2 * delta_time
         self.hitbox_rect.y += self.direction.y * delta_time 
         self.direction.y += self.gravity / 2 * delta_time
         

      self.collision('vertical')
      #jump
      if self.jump:
         #jump only if on floor
         if self.on_surface['floor']:
            self.jump_effect.play()
            self.direction.y = -self.jump_height
            self.timers['wall_slide_block'].activate()
         #wall jump
         elif any((self.on_surface['left'], self.on_surface['right'])) and not self.timers['wall_slide_block'].active:
            self.timers['wall_jump'].activate()
            self.direction.y = -self.jump_height
            if self.on_surface['left']:
               self.direction.x = 0.2
            elif self.on_surface['right']:
               self.direction.x = -0.2
         self.jump = False
   
      self.rect.center = self.hitbox_rect.center

   def surface_contact_check(self):
      #(left, top/bottom) + (x,y), (width, height)
      #temp floor rect
      floor_rect = pygame.Rect(self.hitbox_rect.bottomleft,(self.hitbox_rect.width,2))

      #temp wall rects
      left_wall_rect = pygame.Rect(self.hitbox_rect.topleft + vector(-2, self.hitbox_rect.height/4),(2, self.hitbox_rect.height/2))
      right_wall_rect = pygame.Rect(self.hitbox_rect.topright + vector(0, self.hitbox_rect.height/4),(2, self.hitbox_rect.height/2))

      # #testing contact rect
      # pygame.draw.rect(self.display_surface, 'yellow', floor_rect)
      # pygame.draw.rect(self.display_surface, 'yellow', left_wall_rect)
      # pygame.draw.rect(self.display_surface, 'yellow', right_wall_rect)

      collide_rectangles = [sprite.rect for sprite in self.collision_sprites]

      #contact with the floor
      self.on_surface['floor'] = True if floor_rect.collidelist(collide_rectangles) >= 0 else False

      #contact with the walls
      self.on_surface['left'] = True if left_wall_rect.collidelist(collide_rectangles) >= 0 else False
      self.on_surface['right'] = True if right_wall_rect.collidelist(collide_rectangles) >= 0 else False
      

   def collision(self, axis):
      for sprite in self.collision_sprites:
         if sprite.rect.colliderect(self.hitbox_rect):
            if axis == 'horizontal':
               #left      | |<-----------------------
               if self.hitbox_rect.left <= sprite.rect.right and int(self.old_rect.left) >= int(sprite.old_rect.right):
                  self.hitbox_rect.left = sprite.rect.right
               #right     ----------------------->| |
               if self.hitbox_rect.right >= sprite.rect.left and (self.old_rect.right) <= int(sprite.old_rect.left):
                  self.hitbox_rect.right = sprite.rect.left
               
            else: # vertical
               #top
               if self.hitbox_rect.bottom >= sprite.rect.top and int(self.old_rect.bottom) <= int(sprite.old_rect.top):
                  self.hitbox_rect.bottom = sprite.rect.top
               #bottom
               if self.hitbox_rect.top <= sprite.rect.bottom and int(self.old_rect.top) >= int(sprite.old_rect.bottom):
                  self.hitbox_rect.top = sprite.rect.bottom
            
            self.direction.y = 0
               
               
   def update_timers(self):
      for timer in self.timers.values():
         timer.update()

   def update(self,delta_time):
      self.old_rect = self.hitbox_rect.copy()
      self.update_timers()
      self.input()
      self.move(delta_time)
      self.surface_contact_check()
      # print(self.timers['wall_slide'].active)