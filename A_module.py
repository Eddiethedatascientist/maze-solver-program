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
    """
    Determine the valid points which can be moved. The points
    are valid if they are not explored yet, ie not in explored list.
    """
    potential = []
    for item in point_list:
        if item not in explored:
            potential.append(item)
    return potential

def start_end_points(maze):
    """
    Determine the starting and ending point in 
    the maze
    """
    starting = 0
    ending = 0
    for i, item in enumerate(maze):
        for m, num in enumerate(item):
            if maze[i][m] == "S":
                point = (m, i)
                starting = point
            if maze[i][m] == "T":
                point = (m, i)
                ending = point
    return starting, ending

def manhattan(point_1, point_2):
    """
    Use the manhattan distance as the heuristic
    measurement to find the best possible routes
    along with the actual distance
    """
    x1, y1 = point_1
    x2, y2 = point_2
    distance = abs(x1 - x2) + abs(y1 - y2)
    return distance

def a_star_routing(current, opend, explored, maze, parent, g_dist, end):
    """
    Use the A* search mechanism: with the current state, try to find
    all possible solutions and add them to the opend list, which is for
    nodes which have been explored, but not visited yet. Sort in open to
    find the best node (real distance + heuristic) and update it as the current
    state
    """
    options = neighbourhood(maze, current)
    potent = potential(options, explored)
    for item in potent:
        g_dist[item] = g_dist[current] + 1
        parent[item] = current
        if item not in opend:
            opend.append(item)
    opend.sort(key=lambda point: g_dist[point] + manhattan(point, end))
    current = opend[0]
    x, y = current
    maze[y][x] = "O"
    animation(maze)
    opend.remove(current)
    explored.append(current)
    return current

def reconstruction(current, parent, start):
    """
    Reconstruct the actual route based on the parental relationship
    between each point in reverse. Then, reverse the route to find the solution.
    This function returns the correct route.
    """
    paths = []
    while current != start:
        current = parent[current]
        paths.append(current)
    paths.reverse()
    return paths

def animation(maze):
    os.system("cls")
    for row in maze:
        print(row)
    time.sleep(0.1)
