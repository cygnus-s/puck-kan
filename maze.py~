import pygame
from constants import *

class Maze(object):
    def __init__(self, spritesheet):
        self.spritesheet = spritesheet
        self.spriteInfo = None
        self.rotateInfo = None
        self.images = []
        self.flash_images = []
        self.imageRow = 16

        self.timer = 0
        self.background = None
        self.background_norm = None
        self.background_flash = None
        self.show_normal = True

    def reset(self):
        self.background = self.background_norm
        self.timer = 0
        
    def flash(self, dt):
        self.timer += dt
        if self.timer >= 0.25:
            self.timer = 0
            self.show_normal = not self.show_normal
            if self.show_normal:
                self.background = self.background_norm
            else:
                self.background = self.background_flash
    
    def getMazeImages(self, row=0):
        self.images = []
        self.flash_images = []
        for i in range(11):
            self.images.append(self.spritesheet.getImage(i, self.imageRow+row, TILEWIDTH, TILEHEIGHT))
            self.flash_images.append(self.spritesheet.getImage(i+11, self.imageRow+row, TILEWIDTH, TILEHEIGHT))
            
    def rotate(self, image, value):
        return pygame.transform.rotate(image, value*90)

    def readMazeFile(self, textfile):
        f = open(textfile, "r")
        lines = [line.rstrip('\n') for line in f]
        return [line.split(' ') for line in lines]

    def getMaze(self, mazename):
        self.spriteInfo = self.readMazeFile(mazename+"_sprites.txt")
        self.rotateInfo = self.readMazeFile(mazename+"_rotation.txt")
        
    def constructMaze(self, background, background_flash, row=0):
        self.getMazeImages(row)
        rows = len(self.spriteInfo)
        cols = len(self.spriteInfo[0])
        for row in range(rows):
            for col in range(cols):
                x = col * TILEWIDTH
                y = row * TILEHEIGHT
                val = self.spriteInfo[row][col]
                if val.isdecimal():
                    rotVal = self.rotateInfo[row][col]
                    image = self.rotate(self.images[int(val)], int(rotVal))
                    flash_image = self.rotate(self.flash_images[int(val)], int(rotVal))
                    background.blit(image, (x, y))
                    background_flash.blit(flash_image, (x, y))
                if val == '=':
                    background.blit(self.images[10], (x, y))
                    background_flash.blit(self.flash_images[10], (x, y))
                    
        self.background_norm = background
        self.background_flash = background_flash
        self.background = background
                    
