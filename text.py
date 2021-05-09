import pygame
from vector import Vector2
from constants import *


class Text(object):
    def __init__(self, text, color, x, y, size, show=True):
        self.text = text
        self.color = color
        self.size = size
        self.position = Vector2(x, y)
        self.show = show
        self.label = None
        self.font = None
        self.totalTime = 0
        self.lifespan = 0
        self.setupFont("PressStart2P-vaV7.ttf")
        self.createLabel()

    def setupFont(self, fontpath):
        self.font = pygame.font.Font(fontpath, self.size)

    def createLabel(self):
        self.label = self.font.render(self.text, 1, self.color)

    def setText(self, newtext):
        self.text = newtext
        self.createLabel()

    def update(self, dt):
        if self.lifespan > 0:
            self.totalTime += dt
            if self.totalTime >= self.lifespan:
                self.totalTime = 0
                self.show = False
                self.lifespan = 0

    def render(self, screen):
        if self.show:
            x, y = self.position.asTuple()
            screen.blit(self.label, (x, y))


class TextGroup(object):
    def __init__(self):
        self.textlist = {}
        self.setupText()
        self.tempText = []

    def setupText(self):
        self.textlist["score_label"] = Text("SCORE", WHITE, 0, 0, TILEHEIGHT)
        self.textlist["level_label"] = Text("LEVEL", WHITE, 23 * TILEWIDTH, 0, TILEHEIGHT)
        self.textlist["score"] = Text("0".zfill(8), WHITE, 0, TILEHEIGHT, TILEHEIGHT)
        self.textlist["level"] = Text("0".zfill(3), WHITE, 23 * TILEHEIGHT, TILEHEIGHT, TILEHEIGHT)
        self.textlist["ready"] = Text("READY!", YELLOW, 11.25 * TILEWIDTH, 20 * TILEHEIGHT, TILEHEIGHT, False)
        self.textlist["paused"] = Text("PAUSED!", YELLOW, 10.625 * TILEWIDTH, 20 * TILEHEIGHT, TILEHEIGHT, False)
        self.textlist["gameover"] = Text("GAMEOVER!", RED, 10 * TILEWIDTH, 20 * TILEHEIGHT, TILEHEIGHT, False)

    def update(self, dt):
        if len(self.tempText) > 0:
            tempText = []
            for text in self.tempText:
                text.update(dt)
                if text.show:
                    tempText.append(text)
            self.tempText = tempText

    def updateScore(self, score):
        self.textlist["score"].setText(str(score).zfill(8))

    def updateLevel(self, level):
        self.textlist["level"].setText(str(level).zfill(3))

    def showReady(self):
        self.textlist["ready"].show = True
        self.textlist["paused"].show = False
        self.textlist["gameover"].show = False

    def showPause(self):
        self.textlist["ready"].show = False
        self.textlist["paused"].show = True
        self.textlist["gameover"].show = False

    def showGameOver(self):
        self.textlist["ready"].show = False
        self.textlist["paused"].show = False
        self.textlist["gameover"].show = True

    def hideMessages(self):
        self.textlist["ready"].show = False
        self.textlist["paused"].show = False
        self.textlist["gameover"].show = False

    def createTemp(self, value, position):
        x, y = position.asTuple()
        text = Text(str(value), WHITE, x, y, 8)
        text.lifespan = 1
        self.tempText.append(text)

    def render(self, screen):
        for key in self.textlist.keys():
            self.textlist[key].render(screen)

        for item in self.tempText:
            item.render(screen)
