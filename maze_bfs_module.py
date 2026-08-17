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

def routing(explored, routes, current, maze, history):
    """
    BFS will expand every possible nodes. This function will update
    the path according to the current path in route and update the 
    added point to the explored list. The function return the update
    current level and updated route.
    """
    next_level = []
    for item in current:
        potential_op = []
        options = neighbourhood(maze, item)
        potential_op = potential(options, explored)
        for route in routes:
            if item == route[-1]:
                current_path = route.copy()
                routes.remove(route)
                for x in potential_op:
                    x_cord, y_cord = x
                    update = current_path.copy()
                    update.append(x)
                    explored.append(x)
                    routes.append(update)
                    history.append(update)
                    maze[y_cord][x_cord] = "O"
                    next_level.append(x)
                    animation(maze)
    print(f"Current level: {current}")
    print(f"Next level: {next_level}")
    current = next_level
    next_level = []
    return current, routes

def animation(maze):
    """
    Print the animation of how the algorithm works
    """
    os.system("cls")
    for row in maze:
        print(row)
    time.sleep(0.1)

def decode_track_full(list_track, ending):
    """
    Find out which track has the complete path towards goal
    and use it to update the maze to the finale path
    """
    for item in list_track:
        for point in item:
            if point == ending:
                return item
    