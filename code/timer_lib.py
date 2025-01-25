from pygame.time import get_ticks
class Timer:
   def __init__(self,duratrion, func =None, repeat = False):
      self.start_time = 0
      self.duration = duratrion
      self.func = func
      self.active = False
      self.repeat = repeat

   def activate(self):
      self.active = True
      self.start_time = get_ticks()

   def deactivate(self):
      self.active = False
      self.start_time = 0
      if self.repeat:
         self.activate()
   def update(self):
      current_time = get_ticks()
      if current_time - self.start_time >= self.duration:
         if self.func and self.start_time != 0:
            self.func()
         self.deactivate()