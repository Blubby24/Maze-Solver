from random import random
import pygame
import sys
from Maze import Maze


class Screen:
    def __init__(self, screenSize, nodeSize):
        pygame.init()
        self.surface = pygame.display.set_mode((screenSize[0], screenSize[1]))
        self.surface.fill((0, 0, 0))
        sys.setrecursionlimit(100000)
        self.width, self.height = nodeSize


    def drawLocationOptions(self, start, end):
        pygame.draw.rect(self.surface, (0, 0, 0), pygame.Rect((820, 600), (800, 800)))
        font = pygame.font.Font(pygame.font.get_default_font(), 15)
        text = font.render("Random start/end", True, (255, 255, 255))
        self.surface.blit(text, (850, 600))
        text = font.render("Start", True, (255, 255, 255))
        self.surface.blit(text, (850, 700))
        if start:
            print(start)
            pygame.draw.rect(self.surface, (0,255,0), pygame.Rect(start[1]*self.width, start[0]*self.height, self.width, self.height))
        if end:
            pygame.draw.rect(self.surface, (0,0,255), pygame.Rect(end[1]*self.width, end[0]*self.height, self.width, self.height))
        pygame.display.flip()



    def drawOptions(self):
        pygame.draw.rect(self.surface, (0, 0, 0), pygame.Rect((820, 0), (100, 800)))
        font = pygame.font.Font(pygame.font.get_default_font(), 15)
        write = [font.render("Make Maze", True, (255, 255, 255)), font.render("DepthFirst", True, (255, 255, 255)), font.render("BreadthFirst", True, (255, 255, 255)), font.render("Dijkstra", True, (255, 255, 255), (0, 0, 0)), font.render("AStar", True, (255, 255, 255), (0, 0, 0))]
        x, y = 850, 100
        for text in write:
            self.surface.blit(text, (x, y))
            y += 100
        pygame.display.flip()

    def drawPath(self, path):
        c = (255, 0, 0)
        for coords in path:
            pygame.draw.rect(self.surface, c, pygame.Rect(coords[1] * self.width, coords[0] * self.height, self.width, self.height))
        pygame.display.flip()
        # time.sleep(.01)

    def drawMaze(self, maze):
        self.surface.fill((0, 0, 0))
        color = (255, 255, 255)
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if maze[i][j] == 0:
                    pygame.draw.rect(self.surface, color, pygame.Rect(j * self.width, i * self.height, self.width, self.height))
        pygame.display.flip()
        # time.sleep(.0025)

    def drawStartandEnd(self, start, destination):
        pygame.draw.rect(self.surface, (0, 0, 255),
                         pygame.Rect(destination[1] * self.width, destination[0] * self.height, self.width, self.height))
        pygame.draw.rect(self.surface, (0, 255, 0), pygame.Rect(start[1] * self.width, start[0] * self.height, self.width, self.height))
        pygame.display.flip()

