from math import dist
import os
import time
def neighbourhood (maze, point):
    """
    Determine the possible points right, left, up, down. 4 sides
    """
    neighbourhood = []
    x, y = point
    if x - 1 >= 0:
        if maze[y][x - 1] == ".":
            point = (x - 1, y)
            neighbourhood.append(point)
        elif maze[y][x - 1] == "T":
            point = (x - 1, y)
            if point not in neighbourhood:
                neighbourhood.append(point)
    if y - 1 >= 0:
        if maze[y - 1][x] == ".":
            point = (x, y - 1)
            neighbourhood.append(point)
        elif maze[y - 1][x] == "T":
            point = (x, y - 1)
            if point not in neighbourhood:
                neighbourhood.append(point)
    if y + 1 < len(maze):
        if maze[y + 1][x] == ".":
            point = (x, y + 1)
            neighbourhood.append(point)
        elif maze[y + 1][x] == "T":
            point = (x, y + 1)
            if point not in neighbourhood:
                neighbourhood.append(point)
    for item in maze:
        if x + 1 < len(item):
            if maze[y][x + 1] == ".":
                point = (x + 1, y)
                if point not in neighbourhood:
                    neighbourhood.append(point)
            elif maze[y][x + 1] == "T":
                point = (x + 1, y)
                if point not in neighbourhood:
                    neighbourhood.append(point)
    return neighbourhood

def potential_move(direction_list, explored):
    """
    Determine potential moves in 4 directions. The point must not be
    visited before to be considered acceptable
    """
    potential = []
    for point in direction_list:
        if point not in explored:
            potential.append(point)
    return potential

def ranking(point_list, goal):
    """
    Ranking the potential moves using the Eulide distance.
    The shortest one will be selected as the most promising.
    Eulide method is taken from the Math library. 
    """
    point_list.sort(key=lambda point: dist(point, goal))
    return point_list
    
def start_end_points(maze):
    """
    Determine the starting and ending point in the maze.
    Starting is indicated by the letter "S" while ending is 
    with the letter "T".
    """
    starting = 0
    ending = 0
    for i, item in enumerate(maze):
        for m, num in enumerate(item):
            if item[m] == "S":
                x = m
                y = i
                point = (x, y)
                if starting == 0:
                    starting = point
            if item[m] == "T":
                x = m
                y = i
                point = (x, y)
                if ending == 0:
                    ending = point
    return starting, ending

def route_handling(potential_list, state, path, explored, maze):
    """
    Determine which point to choose when there are moves available
    and handling backtrack when there is a dead end. Intergate the
    change to the interface to track the algorithm.
    """
    if len(potential_list) > 0:
        state = potential_list[0]
        explored.append(state)
        path.append(state)
        x, y = state
        maze[y][x] = "O"
        animation(maze)
        
    else:
        x, y = state
        maze[y][x] = "."
        path.remove(state)
        state = path[len(path) - 1]
        animation(maze)
    return state

def animation(maze):
    """
    Animation for printing the updated maze 
    to visualize the algorithm.
    """
    os.system("cls")
    for row in maze:
        print(row)
    time.sleep(0.1)
