from libraries import *

class ALL_SPRITES(pygame.sprite.Group):
   def __init__(self):
      super().__init__()
      self.display_surf = pygame.display.get_surface()
      
      self.offset_value = vector(0,0)

   def draw(self, player_position):
      self.offset_value.x = -(player_position[0] - WIN_WID/2)
      self.offset_value.y = -(player_position[1] - WIN_HI/2)

      for sprite in sorted(self, key = lambda sprite: sprite.z):
         offset_position = sprite.rect.topleft + self.offset_value
         self.display_surf.blit(sprite.image, offset_position)