from libraries import *
from spirites import Sprite
from timer_lib import Timer
from player import Player
from Groups import ALL_SPRITES
from os.path import join

class Level:
   def __init__(self, tmx_map):#, level_frames):
      self.display_surface = pygame.display.get_surface()

      #groups
      self.all_sprites = ALL_SPRITES()
      self.collision_sprites = pygame.sprite.Group()

      self.setup( tmx_map,)# level_frames)

   #lets setup a tmx map for the level
   def setup(self, tmx_map):#, level_frames):
      for layer in ['BG tiles','BG tiles 2','Terrain']:
         #tiles
         for x,y, surf in tmx_map.get_layer_by_name(layer).tiles():
            groups = [self.all_sprites]
            if layer == 'Terrain':
               groups.append(self.collision_sprites)
            z = Z_axis['BG tiles']
            Sprite((x*TILE_SIZE,y*TILE_SIZE), surf,groups, z)


      #objects
      for obj in tmx_map.get_layer_by_name('objects'):
         if obj.name == 'Astro':      
            self.astro = Player((obj.x,obj.y), self.all_sprites, self.collision_sprites)
         elif obj.name == 'ship':
            ship_surface = pygame.image.load(join('graphics', 'Ship','idle_surface','01.png')).convert_alpha()
            self.ship = Sprite((obj.x, obj.y), ship_surface, [self.all_sprites], Z_axis['objects'])


      for x,y, surf in tmx_map.get_layer_by_name('Magic layer').tiles():
            groups = [self.all_sprites]
            Sprite((x*TILE_SIZE,y*TILE_SIZE), surf,groups, z)


      self.show_msg = False
      self.msg_timer = Timer(20000, self.hide_message)


   def hide_message(self):
      self.show_msg = False

   def display_message(self):
    overlay = pygame.Surface((WIN_WID, WIN_HI), pygame.SRCALPHA)
    overlay.set_alpha(128)  
    overlay.fill((0, 0, 0)) 
    self.display_surface.blit(overlay, (0, 0))
    
    font = pygame.font.Font(None, 36)
    message = font.render("GAME OVER", True, (255, 255, 255))
    text_rect = message.get_rect(center=(WIN_WID // 2, WIN_HI // 2))
    self.display_surface.blit(message, text_rect)




   def run(self, delta_time):
      self.display_surface.fill('black')
      self.all_sprites.update(delta_time)
      self.all_sprites.draw(self.astro.hitbox_rect.center)

      # Collision detection
      if pygame.sprite.collide_rect(self.astro, self.ship):
         self.show_msg = True
         self.msg_timer.activate()
      
      # Show message
      if self.show_msg:
         self.display_message()
      
      self.msg_timer.update()