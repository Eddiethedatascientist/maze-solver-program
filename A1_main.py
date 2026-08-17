from A_module import *
import time
def a_main(maze):
    visited = []
    opened = []
    current_point = 0
    parental = {}
    g_score = {}
    s, e = start_end_points(maze)
    if len(g_score) == 0:
        g_score[s] = 0
    if current_point == 0:
        current_point = s
        start_time = time.perf_counter()
    while current_point != e:
        current_point = a_star_routing(current_point, opened, visited, maze, parental, g_score, e)
        if current_point == e:
            current_point = e
            end_time = time.perf_counter()
            break
    routes = reconstruction(current_point, parental, s)
    run_time = round(end_time - start_time, 3)
    return {
            "Route": routes,
            "Tile searched": len(visited),
            "Route length": len(routes),
            "Run time": run_time
            }
