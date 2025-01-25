from libraries import *

class Sprite(pygame.sprite.Sprite):
   def __init__(self, position, surface = pygame.Surface((TILE_SIZE,TILE_SIZE)), groups = None, z = Z_axis['Terrain']):
      super().__init__(groups)
      self.image = surface
      self.image.set_colorkey((0,0,0))
      self.rect = self.image.get_frect(topleft = position)
      self.old_rect = self.rect.copy()
      self.z = z

class Animation(Sprite):
   def __init__(self, position, frames, groups, z = Z_axis['Terrain'], animation_speed = ANIMATION_SPEED):
      self.frames, = frames
      self.frame_index = 0
      super().__init__(position, self.frames[self.frame_index] , groups, z)

      self.animation_speed = animation_speed

   def animate(self,delta_time):
      self.frame_index += self.animation_speed * delta_time
      self.image = self.frames[int(self.frame_index % len(self.frames))]
   
   def update(self,delta_time):
      self.animate(delta_time)
      