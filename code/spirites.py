from libraries import *

class Sprite(pygame.sprite.Sprite):
   def __init__(self, position, surf, groups):
      super().__init__(groups)
      self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
      self.image.fill('white')
      self.rect = self.image.get_frect(topleft = position)
      self.old_rect = self.rect.copy()