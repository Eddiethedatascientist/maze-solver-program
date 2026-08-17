from dfs_module import *
import time
def dfs_main(maze):
    routes = []
    visited = []
    starting = 0
    ending = 0
    current_state = 0
    starting, ending = start_end_points(maze)
    if current_state == 0:
        current_state = starting
        routes.append(current_state)
        visited.append(current_state)
        start_time = time.perf_counter()
    while current_state != ending:
        next_state = 0
        surround = neighbourhood(maze, current_state)
        positive = potential(surround, visited)
        next_state, routes = select_dfs_route(current_state, positive, maze, visited, routes)
        if next_state != ending:
            current_state = next_state
        else:
            current_state = ending
            end_time = time.perf_counter()
            break
    run_time = round(end_time - start_time, 3)
    return {
        "Route": routes,
        "Tile searched": len(visited),
        "Route length": len(routes),
        "Run time": run_time
    }

    
