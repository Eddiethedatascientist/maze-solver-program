import guilib as ui
import A1_main as a_star
import bfs1_main as bfs
import dfs1_main as dfs
import greedy1_main as g
import os
state = {
    "textbox visual": None,
    "textbox message": None,
    "route": None,
    "algorithm": None,
    "tile explored": None,
    "route length": None,
    "time": None,
    "maze": None,
    "visual maze": None,
    "maze listbox": None,
    "algorithm listbox": None,
    "path": None,
}

def read_data(folder_path, option):
    """
    Read the the maze data as a .txt file and load it onto the program. Use os
    to manage the directory and open the file using the specific path
    """
    chosen_maze = []
    file_path = os.path.join(folder_path, option)
    with open(file_path, "r", encoding="UTF-8") as target:
        for line in target:
            maze_line = line.strip().split()
            chosen_maze.append(maze_line)
    return chosen_maze
    
def open_folder():
    """
    Open the folder to select the file the user wants to load
    """
    folder_path = ui.open_folder_dialog("Load", initial=".")
    return folder_path

def listbox_adding_file(box):
    """
    Adding options to the listbox for the user to choose
    """
    if box.size() > 0:
        ui.open_msg_window("Notice", "Some files already exist, please reset to load other files", error=False)
    else:
        path = open_folder()
        if state["path"] is None:
            state["path"] = path
        maze_list = os.listdir(path)
        for file in maze_list:
            if file.endswith(".txt"):
                ui.add_list_row(box, file)

def list_box_adding_algorithms(box):
    """
    Add the algorithm options to a listbox
    """
    if box.size() > 0:
        ui.open_msg_window("Notice", "Please reset the current options if you want to add other algorithms", error=False)
    else:
        ui.add_list_row(box, "A* search")
        ui.add_list_row(box, "Greedy search")
        ui.add_list_row(box, "BFS")
        ui.add_list_row(box, "DFS")

def selection_algorithms(box):
    """
    Read the selection of algorithm and apply it 
    to the search to find the solutions
    """
    i, selection = ui.read_selected(box)
    return selection

def selecting_maze(box):
    i, option = ui.read_selected(box)
    return option

def load_maze_listbox():
    listbox_adding_file(state["maze listbox"])
    
def load_data_handler():
    """
    This handler function is used for the "Load maze" button. This will load
    the maze data from the txt file and write it into the textbox on the left
    """
    choice = selecting_maze(state["maze listbox"])
    print(choice)
    if choice is None:
        ui.open_msg_window("Error", "Select a maze file first!", error=True)
    else:
        try:
            selected_maze = read_data(state["path"], choice)
        except OSError: 
            ui.open_msg_window("Error", "OS errors, please try again!", error=True)
        except ValueError:
            ui.open_msg_window("Error", "Value errors, please try again!", error=True)
        except Exception:
            ui.open_msg_window("Error", "An exception occurs, please try again!", error=True)
        else:
            state["maze"] = selected_maze
            for row in state["maze"]:
                print(row)
            state["visual maze"] = [row[:] for row in selected_maze]
            draw_maze()

def algorithm_load_handler():
    """
    Handler function to load the algorithms to the listbox
    """
    list_box_adding_algorithms(state["algorithm listbox"])

def draw_maze():
    """
    Draw the current state of the maze to the textbox
    """
    maze = state["visual maze"]
    for i, row in enumerate(maze):
        print_row = " ".join(row)
        if i == 0:
            ui.write_to_textbox(state["textbox visual"], print_row, clear=True)
        else:
            ui.write_to_textbox(state["textbox visual"], print_row, clear=False)

def remove_list_row(box):
    """
    Remove all row in a specific box
    """
    while box.size() > 0:
        ui.remove_list_row(box, 0)
    
def algorithm_handling(selection, maze):
    """
    Function redirect the selection to the desired algorithm which will then 
    be used to solve the maze and return the combo of results
    """
    if selection is None:
        ui.open_msg_window("Error", "Please choose an algorithm to start the solver!", error=True)
        return
    elif selection == "A* search":
        output = a_star.a_main(maze)
    elif selection == "Greedy search":
        output = g.g_main(maze)
    elif selection == "BFS":
        output = bfs.bfs_main(maze)
    elif selection == "DFS":
        output = dfs.dfs_main(maze)
    #Put everything into a string and write it into the textbox
    state["route"] = output["Route"]
    state["tile explored"] = output["Tile searched"]
    state["route length"] = output["Route length"]
    state["time"] = output["Run time"]
    for y, item in enumerate(state["visual maze"]):
        for x, num in enumerate(item):
            point = (x, y)
            if point in state["route"]:
                state["visual maze"][y][x] = "O"
    draw_maze()
    print(state["route"])
    print(state["tile explored"])
    print(state["route length"])
    print(state["time"])
    content = (
        f"Algorithm used: {state["algorithm"]}\n"
        f"Route: {state["route"]}\n"
        f"Total tile explored: {state["tile explored"]}\n"
        f"Route length: {state["route length"]}\n"
        f"Run time: {state["time"]}\n"
    )
    ui.write_to_textbox(state["textbox message"], content, clear=False)

def run_handler():
    """
    Handler function for the button run
    """
    state["algorithm"] = selection_algorithms(state["algorithm listbox"])
    print(state["algorithm"])
    algorithm_handling(state["algorithm"], state["maze"])

def reset_handler():
    """
    Handler function for the button reset_handler
    """
    state["route"] = None
    state["tile explored"] = None
    state["route length"] = None
    state["time"] = None
    state["maze"] = None
    state["visual maze"] = None
    state["algorithm"] = None
    remove_list_row(state["maze listbox"])
    remove_list_row(state["algorithm listbox"])
    ui.write_to_textbox(state["textbox message"], "", clear=True)
    ui.write_to_textbox(state["textbox visual"], "", clear=True)
    
def main():
    window = ui.create_window("Maze solver")
    left_frame = ui.create_frame(window, ui.LEFT)
    right_frame = ui.create_frame(window, ui.RIGHT)
    mazebox_frame = ui.create_frame(left_frame, ui.TOP)
    algobox_frame = ui.create_frame(left_frame, ui.TOP)
    button_frame = ui.create_frame(left_frame, ui.TOP)
    visual_textbox_frame = ui.create_frame(right_frame, ui.TOP)
    result_textbox_frame = ui.create_frame(right_frame, ui.BOTTOM)
    state["maze listbox"] = ui.create_listbox(mazebox_frame, width=80, height=20)
    state["algorithm listbox"] = ui.create_listbox(algobox_frame, width=80, height=20)
    ui.create_button(button_frame, "Load maze", load_maze_listbox)
    ui.create_button(button_frame, "Process maze data", load_data_handler)
    ui.create_button(button_frame, "Load algorithm", algorithm_load_handler)
    ui.create_button(button_frame, "Run", run_handler)
    ui.create_button(button_frame, "Reset", reset_handler)
    ui.create_button(button_frame, "Quit", ui.quit)
    state["textbox visual"] = ui.create_textbox(visual_textbox_frame, width=60, height=40)
    state["textbox message"] = ui.create_textbox(result_textbox_frame, width=60, height=40)
    ui.start()

if __name__ == "__main__":
    main()

