import pygame
from pygame.locals import *
from vector import Vector2
from constants import *
from entity import MazeRunner
from animation import Animation

class Pacman(MazeRunner):
    def __init__(self, nodes, spritesheet):
        MazeRunner.__init__(self, nodes, spritesheet)
        self.name = "pacman"
        self.color = YELLOW
        self.setStartPosition()
        self.lives = 5
        self.startImage = self.spritesheet.getImage(4,0,TILEWIDTH*2, TILEHEIGHT*2)
        self.image = self.startImage
        self.animation = None
        self.animations = {}
        self.defineAnimations()        
        self.lifeicon = self.spritesheet.getImage(0, 1, TILEWIDTH*2, TILEHEIGHT*2)
        self.animateDeath = False
        
    def loseLife(self):
        self.lives -= 1
        self.animation = self.animations["death"]
        self.animateDeath = True

    def reset(self):
        self.setStartPosition()
        self.image = self.startImage
        self.animations["death"].reset()
        self.animateDeath = False
        
    def update(self, dt):
        self.visible = True
        self.position += self.direction*self.speed*dt
        self.updateAnimation(dt)
        direction = self.getValidKey()
        if direction:
            self.moveByKey(direction)
        else:
            self.moveBySelf()

    def updateDeath(self, dt):
        self.image = self.animation.update(dt)
        
    def getValidKey(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_UP]:
            return UP
        if key_pressed[K_DOWN]:
            return DOWN
        if key_pressed[K_LEFT]:
            return LEFT
        if key_pressed[K_RIGHT]:
            return RIGHT
        return None

    def moveByKey(self, direction):
        if self.direction is STOP:
            if self.node.neighbors[direction] is not None:
                self.target = self.node.neighbors[direction]
                self.direction = direction
        else:
            if direction == self.direction * -1:
                self.reverseDirection()
            if self.overshotTarget():
                self.node = self.target
                self.portal()
                if self.node.neighbors[direction] is not None:
                    if self.node.homeEntrance:
                        if self.node.neighbors[self.direction] is not None:
                            self.target = self.node.neighbors[self.direction]
                        else:
                            self.setPosition()
                            self.direction = STOP
                    else:
                        self.target = self.node.neighbors[direction]
                        if self.direction != direction:
                            self.setPosition()
                            self.direction = direction
                else:
                    if self.node.neighbors[self.direction] is not None:
                        self.target = self.node.neighbors[self.direction]
                    else:
                        self.setPosition()
                        self.direction = STOP
                            
    def eatPellets(self, pelletList):
        for pellet in pelletList:
            d = self.position - pellet.position
            dSquared = d.magnitudeSquared()
            rSquared = (pellet.radius+self.collideRadius)**2
            if dSquared <= rSquared:
                return pellet
        return None

    def eatGhost(self, ghosts):
        for ghost in ghosts:
            d = self.position - ghost.position
            dSquared = d.magnitudeSquared()
            rSquared = (self.collideRadius + ghost.collideRadius)**2
            if dSquared <= rSquared:
                return ghost
        return None

    def eatFruit(self, fruit):
        d = self.position - fruit.position
        dSquared = d.magnitudeSquared()
        rSquared = (self.collideRadius+fruit.collideRadius)**2
        if dSquared <= rSquared:
            return True
        return False
    
    def findStartNode(self):
        for node in self.nodes.nodeList:
            if node.pacmanStart:
                return node
        return node
    
    def setStartPosition(self):
        self.direction = LEFT
        self.node = self.findStartNode()
        self.target = self.node.neighbors[self.direction]
        self.setPosition()
        self.position.x -= (self.node.position.x - self.target.position.x) / 2

    def renderLives(self, screen):
        for i in range(self.lives-1):
            x = 10 + (TILEWIDTH*2 + 10) * i
            y = TILEHEIGHT * NROWS - TILEHEIGHT*2
            screen.blit(self.lifeicon, (x, y))

    def defineAnimations(self):
        anim = Animation("loop")
        anim.speed = 30
        anim.addFrame(self.spritesheet.getImage(4, 0, TILEWIDTH*2, TILEHEIGHT*2))
        anim.addFrame(self.spritesheet.getImage(0, 0, TILEWIDTH*2, TILEHEIGHT*2))
        anim.addFrame(self.spritesheet.getImage(0, 1, TILEWIDTH*2, TILEHEIGHT*2))
        anim.addFrame(self.spritesheet.getImage(0, 0, TILEWIDTH*2, TILEHEIGHT*2))
        self.animations["left"] = anim

        anim = Animation("loop")
        anim.speed = 30
        anim.addFrame(self.spritesheet.getImage(4, 0, TILEWIDTH*2, TILEHEIGHT*2))
        anim.addFrame(self.spritesheet.getImage(1, 0, TILEWIDTH*2, TILEHEIGHT*2))
        anim.addFrame(self.spritesheet.getImage(1, 1, TILEWIDTH*2, TILEHEIGHT*2))
        anim.addFrame(self.spritesheet.getImage(1, 0, TILEWIDTH*2, TILEHEIGHT*2))
        self.animations["right"] = anim

        anim = Animation("loop")
        anim.speed = 30
        anim.addFrame(self.spritesheet.getImage(4, 0, TILEWIDTH*2, TILEHEIGHT*2))
        anim.addFrame(self.spritesheet.getImage(2, 0, TILEWIDTH*2, TILEHEIGHT*2))
        anim.addFrame(self.spritesheet.getImage(2, 1, TILEWIDTH*2, TILEHEIGHT*2))
        anim.addFrame(self.spritesheet.getImage(2, 0, TILEWIDTH*2, TILEHEIGHT*2))
        self.animations["down"] = anim

        anim = Animation("loop")
        anim.speed = 30
        anim.addFrame(self.spritesheet.getImage(4, 0, TILEWIDTH*2, TILEHEIGHT*2))
        anim.addFrame(self.spritesheet.getImage(3, 0, TILEWIDTH*2, TILEHEIGHT*2))
        anim.addFrame(self.spritesheet.getImage(3, 1, TILEWIDTH*2, TILEHEIGHT*2))
        anim.addFrame(self.spritesheet.getImage(3, 0, TILEWIDTH*2, TILEHEIGHT*2))
        self.animations["up"] = anim

        anim = Animation("once")
        anim.speed = 10
        anim.addFrame(self.spritesheet.getImage(0, 7, TILEWIDTH*2, TILEHEIGHT*2))
        anim.addFrame(self.spritesheet.getImage(1, 7, TILEWIDTH*2, TILEHEIGHT*2))
        anim.addFrame(self.spritesheet.getImage(2, 7, TILEWIDTH*2, TILEHEIGHT*2))
        anim.addFrame(self.spritesheet.getImage(3, 7, TILEWIDTH*2, TILEHEIGHT*2))
        anim.addFrame(self.spritesheet.getImage(4, 7, TILEWIDTH*2, TILEHEIGHT*2))
        anim.addFrame(self.spritesheet.getImage(5, 7, TILEWIDTH*2, TILEHEIGHT*2))
        anim.addFrame(self.spritesheet.getImage(6, 7, TILEWIDTH*2, TILEHEIGHT*2))
        anim.addFrame(self.spritesheet.getImage(7, 7, TILEWIDTH*2, TILEHEIGHT*2))
        anim.addFrame(self.spritesheet.getImage(8, 7, TILEWIDTH*2, TILEHEIGHT*2))
        anim.addFrame(self.spritesheet.getImage(9, 7, TILEWIDTH*2, TILEHEIGHT*2))
        anim.addFrame(self.spritesheet.getImage(10, 7, TILEWIDTH*2, TILEHEIGHT*2))
        self.animations["death"] = anim

        anim = Animation("static")
        anim.addFrame(self.spritesheet.getImage(4, 0, TILEWIDTH*2, TILEHEIGHT*2))
        self.animations["idle"] = anim

    def updateAnimation(self, dt):
        if self.direction == UP:
            self.animation = self.animations["up"]
        elif self.direction == DOWN:
            self.animation = self.animations["down"]
        elif self.direction == LEFT:
            self.animation = self.animations["left"]
        elif self.direction == RIGHT:
            self.animation = self.animations["right"]
        elif self.direction == STOP:
            self.animation = self.animations["idle"]
        self.image = self.animation.update(dt)
