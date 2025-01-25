from libraries import *

class Sprite(pygame.sprite.Sprite):
   def __init__(self, position, surface = pygame.Surface((TILE_SIZE,TILE_SIZE)), groups = None):
      super().__init__(groups)
      self.image = surface
      # self.image.fill()
      self.rect = self.image.get_frect(topleft = position)
      self.old_rect = self.rect.copy()