import math
from random import random
from PriorityQueue import PriorityQueue


def breadthFirst(graph, start, end , screen):
    queue = [start]
    vistedNodes = set()
    while len(queue) > 0:
        vistedNodes.add(queue[0])
        if queue[0] == end:
            break
        for i, a in enumerate(graph[queue.pop(0)]):
            if a not in vistedNodes:
                queue.append(a)
        screen.drawPath(vistedNodes)


def depthFirst(graph, start, end, screen):
    stack = [start]
    vistedNodes = set()
    while len(stack) > 0:
        if stack[0] in vistedNodes:
            stack.pop(0)
            continue
        if stack[len(stack) - 1] == end:
            break
        vistedNodes.add(stack[len(stack) - 1])
        for i, a in enumerate(graph[stack.pop(len(stack) - 1)]):
            if a in vistedNodes:
                continue
            stack.append(a)
        screen.drawPath(vistedNodes)


def checkPath(graph, start, target):
    stack = [start]
    vistedNodes = set()
    while len(stack) > 0:
        vistedNodes.add(stack[len(stack) - 1])
        if stack[len(stack) - 1] == target:
            break
        for i, a in enumerate(graph[stack.pop(len(stack) - 1)]):
            if a in vistedNodes:
                continue
            stack.append(a)
        # screen.drawPath(vistedNodes)


def shortestPath(m, start, destination, screen):
    screen.drawStartandEnd(start, destination)
    table = {}
    unvisted = set()
    visted = set()
    stack = [start]
    for vertex in m:
        table[vertex] = [math.inf, '']
        unvisted.add(vertex)
    table[start] = [0, '']
    # I should make this a breadth first search it should in theory be faster, but it will look less cool
    while len(stack) > 0:
        # This is depth first
        # current = stack.pop(len(stack) - 1)
        # This is breath first
        current = stack.pop(0)
        visted.add(current)
        unvisted.remove(current)
        screen.drawPath(visted)
        for i, a in enumerate(m[current]):
            if a in unvisted:
                if table[a][0] > table[current][0] + 1:
                    table[a][0] = table[current][0] + 1
                    table[a][1] = current
                stack.append(a)
        if current == destination:
            break
    curr = destination
    path = set()
    while curr != start:
        path.add(curr)
        curr = table[curr][1]
    screen.drawStartandEnd(start, destination)
    return path

    # checkPath(m, start, destination)


def distanceFromNode(vertex, location):
    destX, destY, startX, startY = vertex[1], vertex[0], location[1], location[0]
    return abs(startX - destX) + abs(startY - destY)


def aStar(m, start, destination, screen):
    screen.drawStartandEnd(start, destination)
    table = {}
    unvisted = set()
    visted = set()
    queue = PriorityQueue()
    queue.put(start, 0)
    for vertex in m:
        table[vertex] = [math.inf, '']
        unvisted.add(vertex)
    table[start] = [0, '']
    while queue.size() > 0:
        current = queue.get()
        visted.add(current)
        unvisted.remove(current)
        screen.drawPath(visted)
        if current == destination:
            break
        for i, a in enumerate(m[current]):
            if a in unvisted:
                if table[a][0] > table[current][0] + 1:
                    table[a][0] = table[current][0] + 1
                    table[a][1] = current
                queue.put(a, distanceFromNode(current, destination))
    curr = destination
    path = set()
    while curr != start:
        path.add(curr)
        curr = table[curr][1]
    screen.drawStartandEnd(start, destination)
    return path


def pickRandomStartandEnd(m):
    startX = int(random() * len(m))
    startY = int(random() * len(m[0]))
    while m[startY][startX] == 1:
        startX = int(random() * len(m))
        startY = int(random() * len(m[0]))
    endX = int(random() * len(m))
    endY = int(random() * len(m[0]))
    while m[endY][endX] == 1:
        endX = int(random() * len(m))
        endY = int(random() * len(m[0]))
    return [startY, startX, endY, endX]
