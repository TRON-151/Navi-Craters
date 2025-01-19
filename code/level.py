from settings import *
from spirites import Sprite
from player import Player

class Level:
   def __init__(self, tmx_map):
      self.display_surface = pygame.display.get_surface()

      #groups
      self.all_sprites = pygame.sprite.Group()

      self.setup(tmx_map)

   #setting up the tmx map for each level
   def setup(self, tmx_map):
      for x,y, surf in tmx_map.get_layer_by_name('ground').tiles():
         # print(x,y,surf)
         Sprite((x*TILE_SIZE,y*TILE_SIZE), surf, self.all_sprites)

      for obj in tmx_map.get_layer_by_name('objects'):
         if obj.name == 'ship':      
            Player((obj.x,obj.y), self.all_sprites)

   def run(self):
      self.display_surface.fill('black')
      self.all_sprites.draw(self.display_surface)