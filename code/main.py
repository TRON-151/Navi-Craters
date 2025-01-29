from libraries import *
from level import Level
# from ut import *


from os.path import join

class Game:
   def __init__(self): 
      pygame.init()
      self.display_surface = pygame.display.set_mode((WIN_WID,WIN_HI))
      
      pygame.display.set_caption('Navi Craters')
      self.clock = pygame.time.Clock()

      #W######ill do it later#############
      # self.import_assests()

      self.tmx_maps = {0: load_pygame(join('data','levels','level_0.tmx'))}
      
      #staging each level
      self.current_stage = Level(self.tmx_maps[0])

      #BG sound
      pygame.mixer.music.load(join("audio","space-ambient-sci-fi-121842.mp3"))
      pygame.mixer.music.play(-1) # -1 is for loop


   def run(self):
      while True:
         delta_time = self.clock.tick() / 1000

         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()

         self.current_stage.run(delta_time)
         pygame.display.update()

if __name__ == "__main__":
   game = Game()
   game.run()