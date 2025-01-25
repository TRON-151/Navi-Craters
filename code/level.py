from libraries import *
from spirites import Sprite
from player import Player

class Level:
   def __init__(self, tmx_map,):
      self.display_surface = pygame.display.get_surface()

      #groups
      self.all_sprites = pygame.sprite.Group()
      self.collision_sprites = pygame.sprite.Group()

      self.setup(tmx_map)

   #setting up the tmx map for each level
   def setup(self, tmx_map):
      #tiles
      for x,y, surf in tmx_map.get_layer_by_name('ground').tiles():
         Sprite((x*TILE_SIZE,y*TILE_SIZE), surf, (self.all_sprites, self.collision_sprites))
      #objects
      for obj in tmx_map.get_layer_by_name('objects'):
         if obj.name == 'Astro':      
            Player((obj.x,obj.y), self.all_sprites, self.collision_sprites)


   def run(self, delta_time):
      self.display_surface.fill('black')
      self.all_sprites.update(delta_time)
      self.all_sprites.draw(self.display_surface)