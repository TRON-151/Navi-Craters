import pygame, sys
from pygame.math import Vector2 as vector
from pytmx.util_pygame import load_pygame

WIN_WID, WIN_HI = 520, 360
TILE_SIZE = 16
ANIMATION_SPEED = 6

FPS = 60

Z_axis = {
   'BG tiles': 0,
   'Terrain': 1,
   'objects': 2
}