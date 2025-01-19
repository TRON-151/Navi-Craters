from settings import *
      
class Player(pygame.sprite.Sprite):
   def __init__(self, position, groups):
      super().__init__(groups)
      self.image = pygame.Surface((34,20))
      self.image.fill('red')
      self.rect = self.image.get_frect(topleft = position)