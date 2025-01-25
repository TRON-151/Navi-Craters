from libraries import *
from spirites import Sprite, Animation
from player import Player
from Groups import ALL_SPRITES

class Level:
   def __init__(self, tmx_map, level_frames):
      self.display_surface = pygame.display.get_surface()

      #groups
      self.all_sprites = ALL_SPRITES()
      self.collision_sprites = pygame.sprite.Group()

      self.setup( tmx_map, level_frames)

   #setting up the tmx map for each level
   def setup(self, tmx_map, level_frames):
      for layer in ['BG tiles','Terrain']:
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
            frames = level_frames[obj.name]
            # Animation((obj.x,obj.y), frames, self.all_sprites)



   def run(self, delta_time):
      self.display_surface.fill('black')
      self.all_sprites.update(delta_time)
      self.all_sprites.draw(self.astro.hitbox_rect.center)