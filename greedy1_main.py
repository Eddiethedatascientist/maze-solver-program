from greedy_module import *
import time
def g_main(map_data):
    """
    Main program structure and functions
    """
    current_state = 0
    visited = []
    route = []
    start_point, end_point = start_end_points(map_data)
    if current_state == 0:
        current_state = start_point
        start_time = time.perf_counter()
    while current_state != end_point:
        surround = neighbourhood(map_data, current_state)
        valid_moves = potential_move(surround, visited)
        ranked_valid_moves = ranking(valid_moves, end_point)
        current_state = route_handling(ranked_valid_moves, current_state, route, visited, map_data)
        if current_state == end_point:
            end_time = time.perf_counter()
    run_time = round(end_time - start_time, 3)
    return {
        "Route": route,
        "Tile searched": len(visited),
        "Route length": len(route),
        "Run time": run_time
    }
    