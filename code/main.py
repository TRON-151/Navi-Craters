from settings import *
from level import Level


from os.path import join

class Game:
   def __init__(self):
      pygame.init()
      self.display_surface = pygame.display.set_mode((WIN_WID,WIN_HI))
      pygame.display.set_caption('Navi Craters')


      self.tmx_maps = {0: load_pygame('data/levels/level_0.tmx')}

      self.current_stage = Level(self.tmx_maps[0])
   
   def run(self):
      while True:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()

         self.current_stage.run()
         pygame.display.update()

if __name__ == "__main__":
   game = Game()
   game.run()


   # E:\Uni-Muenster\ITSP\Navi-Craters\data\levels\0.tmx