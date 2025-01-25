from libraries import *
from os import walk
from os.path import join


#platform independent,

def import_image(*path, alpha = True, format = 'png'):
   full_path = join(*path) + f'.{format}'
   if alpha:
      return pygame.image.load(full_path).convert_alpha()
   else:
      return pygame.image.load(full_path).convert()
   
def import_folder(*path):
   frames = []
   for folder_path, subfolders, image_names in walk(join(*path)):
      for image_name in sorted(image_names, key=lambda name: int(name.split('.')[0])):
         full_path = join(folder_path, image_name)
         frames.append(pygame.image.load(full_path).convert_alpha())
   return frames

def import_folder_dict(*path):
   frame_dict = {}
   for folder_path, _, image_names in walk(join(*path)):
      for image_name in image_names:
         full_path = join(folder_path, image_name)
         surface = pygame.image.load(full_path).convert_alpha()
         frame_dict[image_name.split('.'[0])] = surface
   return frame_dict

def import_sub_folders(*path):
   frame_dict = {}
   for _, subfolders, __ in walk(join(*path)):
      if subfolders:
         for subfolder in subfolders:
            frame_dict[subfolder] = import_folder(*path, subfolder)
   return frame_dict