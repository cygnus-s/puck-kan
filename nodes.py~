import pygame
from vector import Vector2
from constants import *
from stack import Stack

class Node(object):
    def __init__(self, row, column):
        self.row, self.column = row, column
        self.position = Vector2(column*TILEWIDTH, row*TILEHEIGHT)
        self.neighbors = {UP:None, DOWN:None, LEFT:None, RIGHT:None}
        self.portalNode = None
        self.portalVal = 0
        self.homeGuide = False
        self.homeEntrance = False
        self.spawnNode = False
        self.pacmanStart = False
        self.fruitStart = False
        
    def render(self, screen):
        for n in self.neighbors.keys():
            if self.neighbors[n] is not None:
                line_start = self.position.asTuple()
                line_end = self.neighbors[n].position.asTuple()
                pygame.draw.line(screen, WHITE, line_start, line_end, 4)
                if not self.homeEntrance and not self.spawnNode:
                    pygame.draw.circle(screen, RED, self.position.asInt(), 12)
                else:
                    pygame.draw.circle(screen, WHITE, self.position.asInt(), 12)

class NodeGroup(object):
    def __init__(self, level):
        self.nodeList = []
        self.homeList = []
        self.level = level
        self.grid = None
        self.nodeStack = Stack()
        self.pathSymbols = ["p", "P"]
        self.portalSymbols = ["1", "2"]####
        self.nodeSymbols = ["+", "n", "N", "H", "S", "Y", "F"] + self.portalSymbols
        self.grid = self.readMazeFile(level)
        self.homegrid = self.getHomeArray()
        self.createNodeList(self.grid, self.nodeList)
        self.createNodeList(self.homegrid, self.homeList)
        self.setupPortalNodes()
        self.moveHomeNodes()
        self.homeList[0].homeEntrance = True
        
    def getHomeArray(self):
        return [['0', '0', '+', '0', '0'],
                ['0', '0', '|', '0', '0'],
                ['+', '0', '|', '0', '+'],
                ['+', '-', 'S', '-', '+'],
                ['+', '0', '0', '0', '+']]

    def readMazeFile(self, textfile):
        f = open(textfile, "r")
        lines = [line.rstrip('\n') for line in f]
        return [line.split(' ') for line in lines]
    
    def createNodeList(self, grid, nodeList):
        startNode = self.findFirstNode(grid)
        self.nodeStack.push(startNode)
        while not self.nodeStack.isEmpty():
            node = self.nodeStack.pop()
            self.addNode(node, nodeList)
            leftNode = self.getPathNode(LEFT, node.row, node.column-1, nodeList, grid)
            rightNode = self.getPathNode(RIGHT, node.row, node.column+1, nodeList, grid)
            upNode = self.getPathNode(UP, node.row-1, node.column, nodeList, grid)
            downNode = self.getPathNode(DOWN, node.row+1, node.column, nodeList, grid)
            node.neighbors[LEFT] = leftNode
            node.neighbors[RIGHT] = rightNode
            node.neighbors[UP] = upNode
            node.neighbors[DOWN] = downNode
            self.addNodeToStack(leftNode, nodeList)
            self.addNodeToStack(rightNode, nodeList)
            self.addNodeToStack(upNode, nodeList)
            self.addNodeToStack(downNode, nodeList)

    def findFirstNode(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        nodeFound = False
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] in self.nodeSymbols:
                    node = Node(row, col)
                    if grid[row][col] in self.portalSymbols:
                        node.portalVal = grid[row][col]
                    return node
        return None
    
    def getNode(self, x, y, nodeList=[]):
        for node in nodeList:
            if node.position.x == x and node.position.y == y:
                return node
        return None
    
    def getNodeFromNode(self, node, nodeList):
        if node is not None:
            for inode in nodeList:
                if node.row == inode.row and node.column == inode.column:
                    return inode
        return node
    
    def getPathNode(self, direction, row, col, nodeList, grid):
        tempNode = self.followPath(direction, row, col, grid)
        return self.getNodeFromNode(tempNode, nodeList)

    def addNode(self, node, nodeList):
        nodeInList = self.nodeInList(node, nodeList)
        if not nodeInList:
            nodeList.append(node)
            
    def addNodeToStack(self, node, nodeList):
        if node is not None and not self.nodeInList(node, nodeList):
            self.nodeStack.push(node)
            
    def nodeInList(self, node, nodeList):
        for inode in nodeList:
            if node.position.x == inode.position.x and node.position.y == inode.position.y:
                return True
        return False

    def followPath(self, direction, row, col, grid):
        rows = len(grid)
        columns = len(grid[0])
        if direction == LEFT and col >= 0:
            return self.pathToFollow(LEFT, row, col, "-", grid)
        elif direction == RIGHT and col < columns:
            return self.pathToFollow(RIGHT, row, col, "-", grid)
        elif direction == UP and row >= 0:
            return self.pathToFollow(UP, row, col, "|", grid)
        elif direction == DOWN and row < rows:
            return self.pathToFollow(DOWN, row, col, "|", grid)
        else:
            return None
        
    def pathToFollow(self, direction, row, col, path, grid):
        tempSymbols = [path]+self.nodeSymbols + self.pathSymbols
        if grid[row][col] in tempSymbols:
            while grid[row][col] not in self.nodeSymbols:
                if direction is LEFT: col -= 1
                elif direction is RIGHT: col += 1
                elif direction is UP: row -= 1
                elif direction is DOWN: row += 1
            node = Node(row, col)
            if grid[row][col] == "H":
                node.homeGuide = True
            if grid[row][col] == "S":
                node.spawnNode = True
            if grid[row][col] == "Y":
                node.pacmanStart = True
            if grid[row][col] == "F":
                node.fruitStart = True
            if grid[row][col] in self.portalSymbols:
                node.portalVal = grid[row][col]
            return node
        else:
            return None

    def setupPortalNodes(self):
        portalDict = {}
        for i in range(len(self.nodeList)):
            if self.nodeList[i].portalVal != 0:
                if self.nodeList[i].portalVal not in portalDict.keys():
                    portalDict[self.nodeList[i].portalVal] = [i]
                else:
                    portalDict[self.nodeList[i].portalVal] += [i]
        for key in portalDict.keys():
            node1, node2 = portalDict[key]
            self.nodeList[node1].portalNode = self.nodeList[node2]
            self.nodeList[node2].portalNode = self.nodeList[node1]

    def moveHomeNodes(self):
        print("Move home nodes")
        for node in self.nodeList:
            if node.homeGuide:
                nodeA = node
                break
        nodeB = nodeA.neighbors[LEFT]
        mid = (nodeA.position + nodeB.position) / 2.0
        mid = Vector2(int(mid.x), int(mid.y))
        vec = Vector2(self.homeList[0].position.x, self.homeList[0].position.y)
        #print("Number of nodes: " + str(len(self.nodeList)))
        #print("Number of home nodes: " + str(len(self.homeList)))
        
        for node in self.homeList:
            node.position -= vec
            node.position += mid
            self.addNode(node, self.nodeList)###
            
        #print("Number of nodes: " + str(len(self.nodeList)))
        #print("Node A: " + str(nodeA.position) + " <==== " + str(nodeA.neighbors[LEFT].position))
        #print("Node B: " + str(nodeB.position) + " ====> " + str(nodeB.neighbors[RIGHT].position))

        A = self.getNodeFromNode(nodeA, self.nodeList)
        #print(N.position)
        B = self.getNodeFromNode(nodeB, self.nodeList)
        #print(N.position)
        H = self.getNodeFromNode(self.homeList[0], self.nodeList)
        #print(N.position)
        #print("")
        A.neighbors[LEFT] = H
        B.neighbors[RIGHT] = H
        H.neighbors[RIGHT] = A
        H.neighbors[LEFT] = B
        
        #nodeA.neighbors[LEFT] = self.homeList[0]
        #nodeB.neighbors[RIGHT] = self.homeList[0]
        #self.homeList[0].neighbors[RIGHT] = nodeA
        #self.homeList[0].neighbors[LEFT] = nodeB


        
        #print("")
        #print("Node A: " + str(nodeA.position) + " <==== " + str(nodeA.neighbors[LEFT].position))
        #print("Node B: " + str(nodeB.position) + " ====> " + str(nodeB.neighbors[RIGHT].position))

        #print("")
        #A = self.getNode(144, 224, self.nodeList)
        #print(A.position)
        #print(A.neighbors[RIGHT].position)


        
    def render(self, screen):
        for node in self.nodeList:
            node.render(screen)
        for node in self.homeList:
            node.render(screen)
