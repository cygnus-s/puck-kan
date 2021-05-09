import pygame
from constants import *

class Spritesheet(object):
    def __init__(self):
        self.sheet = pygame.image.load("spritesheet.png").convert()
        self.sheet.set_colorkey(TRANSPARENT)

    def getImage(self, x, y, width, height):
        x *= width
        y *= height
        self.sheet.set_clip(pygame.Rect(x, y, width, height))
        return self.sheet.subsurface(self.sheet.get_clip())
