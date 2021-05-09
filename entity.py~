import pygame
from vector import Vector2
from constants import *

class MazeRunner(object):
    def __init__(self, nodes, spritesheet):
        self.name = ""
        self.direction = STOP
        self.speed = 100
        self.radius = 10
        self.collideRadius = 5
        self.color = WHITE
        self.nodes = nodes
        self.node = nodes.nodeList[0]
        self.target = self.node
        self.setPosition()
        self.visible = True
        self.image = None
        self.spritesheet = spritesheet
    
    def setPosition(self):
        self.position = self.node.position.copy()
        
    def update(self, dt):
        self.position += self.direction*self.speed*dt
        self.moveBySelf()

    def moveBySelf(self):
        if self.direction is not STOP:
            if self.overshotTarget():
                self.node = self.target
                self.portal()
                if self.node.neighbors[self.direction] is not None:
                    self.target = self.node.neighbors[self.direction]
                else:
                    self.setPosition()
                    self.direction = STOP
                    
    def overshotTarget(self):
        if self.target is not None:
            vec1 = self.target.position - self.node.position
            vec2 = self.position - self.node.position
            node2Target = vec1.magnitudeSquared()
            node2Self = vec2.magnitudeSquared()
            return node2Self >= node2Target
        return False


    def reverseDirection(self):
        if self.direction is UP: self.direction = DOWN
        elif self.direction is DOWN: self.direction = UP
        elif self.direction is LEFT: self.direction = RIGHT
        elif self.direction is RIGHT: self.direction = LEFT
        temp = self.node
        self.node = self.target
        self.target = temp

    def portal(self):
        if self.node.portalNode:
            self.node = self.node.portalNode
            self.setPosition()

    def render(self, screen):
        if self.visible:
            if self.image is not None:
                p = self.position.asTuple()
                p = (p[0]-TILEWIDTH/2, p[1]-TILEWIDTH/2)
                screen.blit(self.image, p)
            else:
                p = self.position.asInt()
                pygame.draw.circle(screen, self.color, p, self.radius)

                        
