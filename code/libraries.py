import pygame, sys
from pygame.math import Vector2 as vector
from pytmx.util_pygame import load_pygame

WIN_WID, WIN_HI = 520, 360
TILE_SIZE = 16

FPS = 60

#utilize this later for more layers
Z_axis = {
   'BG tiles': 0,
   'BG tiles 2': 1,
   'Terrain': 2,
   'objects': 3
}