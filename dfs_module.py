import os
import time
def neighbourhood(maze, point):
    """
    Determine the surrounding points if they are within 
    the limits. The valid moves are right, left, up and down
    and the route is goable, ie "." . The function returns a list of point.
    """
    neigbour = []
    x, y = point
    if x - 1 >= 0:
        if maze[y][x - 1] == ".":
            point = (x - 1, y)
            neigbour.append(point)
        elif maze[y][x - 1] == "T":
            point = (x - 1, y)
            if point not in neigbour:
                neigbour.append(point)
    if y - 1 >= 0:
        if maze[y - 1][x] == ".":
            point = (x, y - 1)
            neigbour.append(point)
        elif maze[y - 1][x] == "T":
            point = (x, y - 1)
            if point not in neigbour:
                neigbour.append(point)
    if y + 1 < len(maze):
        if maze[y + 1][x] == ".":
            point = (x, y + 1)
            neigbour.append(point)
        elif maze[y + 1][x] == "T":
            point = (x, y + 1)
            if point not in neigbour:
                neigbour.append(point)
    for item in maze:
        if x + 1 < len(item):
            if maze[y][x + 1] == ".":
                point = (x + 1, y)
                if point not in neigbour:
                    neigbour.append(point)
            elif maze[y][x + 1] == "T":
                point = (x + 1, y)
                if point not in neigbour:
                    neigbour.append(point)
    return neigbour

def potential(point_list, explored):
    potential = []
    for item in point_list:
        if item not in explored:
            potential.append(item)
    return potential

def start_end_points(maze):
    """
    Determine the valid points which can be moved. The points
    are valid if they are not explored yet, ie not in explored list.
    """
    start = 0
    end = 0
    for i, item in enumerate(maze):
        for m, num in enumerate(item):
            if item[m] == "S":
                point = (m, i)
                if start == 0:
                    start = point
            if item[m] == "T":
                point = (m, i)
                if end == 0:
                    end = point
    return start, end

def select_dfs_route(current, poten_list, maze, explored, paths):
    """
    Use the DFS structure method. Go deep into a single path until
    no other valid nodes are present. Then, backtrack until find a possible
    node and then go deep into it again with similar mechanism. The function
    returns the current state and the path to that state
    """
    if len(poten_list) > 0:
        current = poten_list[0]
        paths.append(current)
        explored.append(current)
        x, y = current
        maze[y][x] = "O"
        animation(maze)
    else:
        x, y = current
        maze[y][x] = "."
        animation(maze)
        paths.remove(current)
        current = paths[-1]
        options = neighbourhood(maze, current)
        new_potent = potential(options, explored)
        if len(options) == 0:
            x, y = current
            maze[y][x] = "."
            animation(maze)
            paths.remove(current)
            current = paths[-1]
        else:
            if len(new_potent) == 0:
                x, y = current
                maze[y][x] = "."
                animation(maze)
                paths.remove(current)
                current = paths[-1]
    return current, paths

def animation(maze):
    os.system("cls")
    for row in maze:
        print(row)
    time.sleep(0.1)
    