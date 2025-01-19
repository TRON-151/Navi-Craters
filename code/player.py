from settings import *
      
class Player(pygame.sprite.Sprite):
   def __init__(self, position, groups):
      super().__init__(groups)
      self.image = pygame.Surface((34,20)) # pixel size of ship
      self.image.fill('red')
      self.rect = self.image.get_frect(topleft = position)

      #movement
      self.direction = vector()
      self.speed = 200

   def input(self):
      keys = pygame.key.get_pressed()

      input_vector = vector(0,0)

      if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
         input_vector.x += 1

      if keys[pygame.K_a] or keys[pygame.K_LEFT]:
         input_vector.x -= 1

      self.direction = input_vector.normalize() if input_vector else input_vector



   def move(self,dt):
      self.rect.topleft += self.direction * self.speed * dt
      pass

   def update(self,delta):
      self.input()
      self.move(delta)