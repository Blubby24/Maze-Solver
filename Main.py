from random import random
import pygame
from Screen import Screen
import Pathfinding
from Maze import Maze

screen = Screen((1000, 800), (3, 3))


def pickRandomStartandEnd(m):
    startX, startY, endX, endY = int(random() * len(m)), int(random() * len(m[0])), int(random() * len(m)), int(
        random() * len(m[0]))
    while m[startY][startX] == 1 or m[endY][endX] == 1:
        startX, startY, endX, endY = int(random() * len(m)), int(random() * len(m[0])), int(random() * len(m)), int(
            random() * len(m[0]))
    return (startY, startX), (endY, endX)


def makeMaze(width, height):
    m = Maze(width, height)
    screen.drawMaze(m.maze)
    return m


def pickStartandEnd(m):
    notPicked = True
    start, end = None, None
    while notPicked:
        screen.drawLocationOptions(start, end)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                notPicked = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                coords = pygame.mouse.get_pos()
                mouse = pygame.Rect(coords, (1, 1))
                startButton = pygame.Rect((850, 700), (150, 75))
                randomButton = pygame.Rect((850, 600), (150, 75))
                if start and end and startButton.contains(mouse):
                    return start, end
                if randomButton.contains(mouse):
                    start, end = pickRandomStartandEnd(m)
                if start and not end and (0 <= coords[0] <= 250 * screen.width and 0 <= coords[1] <= 250 * screen.height):
                    if m[int(coords[0] / screen.height)][int(coords[1] / screen.width)] == 0:
                        end = int(coords[1] / screen.height), int(coords[0] / screen.width)
                if not start and (0 <= coords[0] <= 250 * screen.width and 0 <= coords[1] <= 250 * screen.height):
                    if m[int(coords[0]/screen.height)][int(coords[1]/screen.width)] == 0:
                        start = int(coords[1]/screen.width), int(coords[0]/screen.height)



def pickOption(coords):
    mouse = pygame.Rect(coords, (1, 1))
    x, y = 820, 100
    for i in range(6):
        if pygame.Rect((x, y), (150, 75)).contains(mouse):
            print(i)
            return i
        y += 100
    return -1


keepGameRunning = True

mazeActive = False
selectingLocation = False

while keepGameRunning:
    screen.drawOptions()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGameRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            option = pickOption(pygame.mouse.get_pos())
            if option == -1:
                continue
            if option == 0:
                maze = makeMaze(250, 250)
                screen.drawMaze(maze.maze)
                mazeActive = True
            if option == 1 and mazeActive:
                start, end = pickStartandEnd(maze.maze)
                screen.drawStartandEnd(start, end)
                Pathfinding.depthFirst(maze.adjList, start, end, screen)
                screen.drawStartandEnd(start, end)
                mazeActive = False
            if option == 2 and mazeActive:
                start, end = pickStartandEnd(maze.maze)
                screen.drawStartandEnd(start, end)
                Pathfinding.breadthFirst(maze.adjList, start, end, screen)
                screen.drawStartandEnd(start, end)
                mazeActive = False
            if option == 3 and mazeActive:
                start, end = pickStartandEnd(maze.maze)
                screen.drawStartandEnd(start, end)
                path = Pathfinding.shortestPath(maze.adjList, start, end, screen)
                screen.drawStartandEnd(start, end)
                screen.drawMaze(maze.maze)
                screen.drawPath(path)
                screen.drawStartandEnd(start, end)
                mazeActive = False
            if option == 4 and mazeActive:
                start, end = pickStartandEnd(maze.maze)
                screen.drawStartandEnd(start, end)
                path = Pathfinding.aStar(maze.adjList, start, end, screen)
                screen.drawStartandEnd(start, end)
                screen.drawMaze(maze.maze)
                screen.drawPath(path)
                screen.drawStartandEnd(start, end)
                mazeActive = False
            print(pygame.mouse.get_pos())
