from maze_bfs_module import *
import time
def bfs_main(maze):
    current_level = 0
    visited = []
    paths = []
    records = []
    start, end = start_end_points(maze)
    if start not in records:
        level_0 = []
        level_0.append(start)
        start_time = time.perf_counter()
        if start not in visited:
            visited.append(start)
        if level_0 not in records:
            records.append(level_0)
    if current_level == 0:
        current_level = neighbourhood(maze, start)
        for x in current_level:
            level_1 = []
            level_1.append(start)
            level_1.append(x)
            if x not in visited:
                visited.append(x)
            if level_1 not in records:
                records.append(level_1)
            if level_1 not in paths:
                paths.append(level_1)
            hor, ver = x
            maze[ver][hor] = "O"
            animation(maze)
    while True:
        current_level, paths = routing(visited, paths, current_level, maze, records)
        if end in current_level:
            end_time = time.perf_counter()
            break
    run_time = round(end_time - start_time, 3)
    for item in paths:
        for point in item:
            if point == end:
                correct_route = item
            
    return {
            "Route": correct_route,
            "Tile searched": len(visited),
            "Route length": len(correct_route),
            "Run time": run_time
        }
