from libraries import *
      
class Player(pygame.sprite.Sprite):
   def __init__(self, position, groups, collision_sprites):
      super().__init__(groups)
      self.image = pygame.Surface((34,20)) # pixel size of ship
      self.image.fill('red')

      #player rect
      self.rect = self.image.get_frect(topleft = position)
      self.old_rect = self.rect.copy()

      #movement
      self.direction = vector()
      self.speed = 200
      self.gravity = 300

      #collision
      self.collision_sprites = collision_sprites


   def input(self):
      keys = pygame.key.get_pressed()

      input_vector = vector(0,0)
      
      #---------> 
      if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
         input_vector.x += 1
      # <---------
      if keys[pygame.K_a] or keys[pygame.K_LEFT]:
         input_vector.x -= 1

      self.direction.x = input_vector.normalize().x if input_vector else 0
      #jump
      if keys[pygame.K_SPACE]:
         self.direction.y = -10


   def move(self,delta_time):
      #horizontal movement
      self.rect.x += self.direction.x * self.speed * delta_time
      self.collision('horizontal')


      #vertical movement
      self.direction.y += self.gravity / 2 * delta_time


      self.rect.y += self.direction.y * delta_time #* self.speed 
      self.direction.y += self.gravity / 2 * delta_time
      
      self.collision('vertical')

   def collision(self, axis):
      for sprite in self.collision_sprites:
         if sprite.rect.colliderect(self.rect):
            if axis == 'horizontal':
               #left      | |<-----------------------
               if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                  self.rect.left = sprite.rect.right
               #right     ----------------------->| |
               if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                  self.rect.right = sprite.rect.left
               
            else: # vertical
               #top
               if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                  self.rect.bottom = sprite.rect.top
               #bottom
               if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                  self.rect.top = sprite.rect.bottom
            
            self.direction.y = 0
               
               


   def update(self,delta_time):
      self.old_rect = self.rect.copy()
      self.input()
      self.move(delta_time)