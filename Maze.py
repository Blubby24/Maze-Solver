from random import shuffle, random


class Maze:
    def __init__(self, width, height):
        self.maze = self.generateMaze(width, height)
        self.adjList = self.mazeToAdjacencyList(self.maze)

    def initializeMaze(self, width, height):
        maze = []
        for i in range(height):
            maze.append([])
            for j in range(width):
                maze[i].append(1)
        x = int(random() * width) - 1
        y = int(random() * height) - 1
        if x % 2 == 0:
            if x == width:
                x -= 1
            else:
                x += 1
        if y % 2 == 0:
            if y == height:
                y -= 1
            else:
                y += 1
        return maze, x, y

    def generateMaze(self, width, height):
        maze, r, c = self.initializeMaze(width, height)
        maze[r][c] = 0
        self.helper(r, c, maze)
        return maze

    def helper(self, r, c, m):
        direction = [0, 1, 2, 3]
        shuffle(direction)
        # print(direction)
        for i, d in enumerate(direction):
            # Direction 0 is up
            if d == 0:
                if r - 2 <= 0:
                    continue
                if m[r - 2][c] != 0:
                    m[r - 1][c] = 0
                    m[r - 2][c] = 0
                    # drawMaze(m)
                    self.helper(r - 2, c, m)
            # Direction 1 is right
            if d == 1:
                if c + 2 >= len(m[0]):
                    continue
                if m[r][c + 2] != 0:
                    m[r][c + 1] = 0
                    m[r][c + 2] = 0
                    # drawMaze(m)
                    self.helper(r, c + 2, m)
            # Direction 2 is down
            if d == 2:
                if r + 2 >= len(m):
                    continue
                if m[r + 2][c] != 0:
                    m[r + 1][c] = 0
                    m[r + 2][c] = 0
                    # rawMaze(m)
                    self.helper(r + 2, c, m)
            # Direction 3 is up
            if d == 3:
                if c - 2 <= 0:
                    continue
                if m[r][c - 2] != 0:
                    m[r][c - 1] = 0
                    m[r][c - 2] = 0
                    # drawMaze(m)
                    self.helper(r, c - 2, m)

    def mazeToAdjacencyList(self, m):
        res = {}
        for r in range(len(m)):
            for c in range(len(m[r])):
                coords = r, c
                res[coords] = []
                if r - 1 >= 0 and m[r - 1][c] != 1:
                    res[coords].append((r - 1, c))
                if r + 1 < len(m) and m[r + 1][c] != 1:
                    res[coords].append((r + 1, c))
                if c - 1 >= 0 and m[r][c - 1] != 1:
                    res[coords].append((r, c - 1))
                if c + 1 < len(m[r]) and m[r][c + 1] != 1:
                    res[coords].append((r, c + 1))
        return res
