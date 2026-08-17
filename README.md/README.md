## Maze Solver & Algorithm Solver and Visualization Tool ##
## 1. Project description ##

A Python application for loading, visualizing, and solving maze problems using multiple pathfinding algorithms. The application provides a graphical user interface for selecting maze data, choosing a search algorithm, running the solver, and displaying the resulting path and performance metrics.

## 2. Project Overview ##

The project was developed as a personal project to consolidate and visualize knowledge from the Introduction to AI course at the University of Oulu, with a particular focus on search algorithms.

The application allows users to load maze data from external .txt files, select a search algorithm, solve the maze, visualize the resulting path, and display algorithm performance metrics through a graphical user interface.

The application supports four pathfinding algorithms, implemented from scratch:

A* Search
Greedy Search
Breadth-First Search (BFS)
Depth-First Search (DFS)

Maze data is stored externally as .txt files and can be loaded into the application. The selected algorithm processes the maze and returns the discovered route together with information about the search process and execution performance.

## 3. Specific features ##

Features
Load maze files from an external folder
Support .txt maze data
Process and validate maze data
Select between multiple pathfinding algorithms
Implement A* Search from scratch
Implement Greedy Search from scratch
Implement Breadth-First Search from scratch
Implement Depth-First Search from scratch
Visualize the maze and explored tiles
Display the discovered route
Display the number of explored tiles
Display route length
Measure algorithm runtime
Reset the application state
Use a modular program structure
Run all supported algorithms through a single GUI platform

<img width="752" height="764" alt="Product result" src="https://github.com/user-attachments/assets/7b44d555-151e-407f-8e12-00e6e0d19d7a" />

## 4. Supported Algorithms ##

### A* Search ###

A* Search combines the actual cost of reaching a node with a heuristic estimate of the remaining distance.

The algorithm prioritizes nodes using:

f(n) = g(n) + h(n)

where:

g(n) is the cost from the starting point to the current node
h(n) is the estimated cost from the current node to the target
f(n) is the total estimated cost

### Greedy Search ###

Greedy Search selects the node that appears to be closest to the target according to the heuristic function.

The algorithm focuses primarily on:

h(n): heuristic is determined based on the Eulide distance

This allows it to make fast decisions, although the resulting route is not necessarily optimal.

### Breadth-First Search (BFS) ###

BFS explores the maze level by level.

The implementation maintains visited positions, possible paths, search levels, and route records until the destination is reached.

### Depth-First Search (DFS) ###

DFS explores one path as deeply as possible before backtracking and continuing with another available path.

It demonstrates a fundamentally different search strategy compared with BFS and heuristic-based algorithms.

## Algorithm Comparison ##

The application allows the same maze to be solved using different algorithms, making it possible to compare their behaviour.

| Algorithm | Search Strategy | Shortest Path Guarantee | Heuristic |
|---|---|---|---|
| A* Search | Cost + heuristic | Yes, under appropriate conditions | Yes |
| Greedy Search | Heuristic-driven | No | Yes |
| BFS | Level-by-level | Yes, for unweighted mazes | No |
| DFS | Depth-first | No | No |

The application reports:

Number of explored tiles
Route length
Execution time

This makes the project useful not only as a maze solver, but also as a small platform for observing differences between search algorithms.
## 4. Application architecture ##

The project follows a modular structure where different responsibilities are separated into individual modules.
<img width="1536" height="1024" alt="ChatGPT Image Aug 17, 2026, 03_03_18 PM" src="https://github.com/user-attachments/assets/7638220a-90fa-4b3d-8a64-6b0893d230f7" />

## 5.Project Structure ##

Maze-Solver

### Main program ###
visualization.py
guilib.py

### A* modules ###
A1_main.py
A1_module.py

### Greedy modules ###
 greedy1_main.py
 greedy1_module.py

### BFS modules ###
 bfs1_main.py
 maze_bfs_module.py

### DFS modules ###
dfs1_main.py
dfs1_module.py

### Measurement files (Optional, you can put your own files) ###
maze_01_easy.txt
maze_02_medium.txt
maze_03_large.txt
maze_04_dead_end.txt
maze_05_complex.txt

Maze data is stored externally in .txt files.

Each maze consists of a grid containing symbols representing different types of cells.

Example:

S . . # . .
# # . # . #
. . . . . #
. # # # . #
. . . # . T
The exact module structure may evolve as the project continues to be developed. All of the codes can be found in the src folder in the repository.

## 6. Output ##

After solving a maze, the application displays:

Algorithm used: BFS

Route: [(0, 0), (1, 0), (2, 0), ...]

Total tile explored: 68

Route length: 21

Run time: 8.72

The maze visualization also shows the explored search area and the resulting path.

## 7. Performance metrics ##

| Metric |	Description |
| Route |	The sequence of coordinates from start to target |
| Total tiles explored |	Number of tiles visited during the search |
| Route length |	Number of positions in the resulting route |
| Run time |	Execution time measured using Python's time.perf_counter() |

These metrics make it possible to compare how different algorithms behave when solving the same maze.

## 8. Technologies Used ##

Python
Tkinter
File I/O
Modular Programming
Object / State-based program organization
Search Algorithms
Heuristic Search
Graph Search

## 9. Key Concepts ##

This project was built to reinforce practical understanding of:

State-space search
Search trees
Graph traversal
Path reconstruction
Visited states
Frontier management
Heuristic-based search
A* Search
Greedy Best-First Search
Breadth-First Search
Depth-First Search
Algorithm performance comparison
Modular software architecture
GUI event handling
External data loading

## 10. Current Version ##

Version 1.0 — Initial Complete Application

The first complete version of the project provides an end-to-end working application:

Maze files can be loaded from an external directory
Maze data can be processed and stored in application state
Search algorithms can be selected through the GUI
Four search algorithms are implemented
Search results are returned through a common output structure
The explored maze can be visualized
The final route is reconstructed
Performance metrics are calculated
Results are displayed in the GUI
The application can be reset and reused with different maze datasets
The stand alone version which works without cmd interference

This version establishes the core architecture of the project.

## 11. Future Improvements ##

The next development stage will focus on improving the usability, visualization, and robustness of the application.

Planned improvements include:

Animated search visualization directly inside the GUI
Step-by-step visualization of algorithm exploration
Improved GUI layout and styling
Better result formatting
Input validation for invalid maze files
Error messages for invalid user operations
Handling cases where no valid route exists
Algorithm comparison mode
Visualization of heuristic values for A* and Greedy Search
Visualization of search frontier / open sets
More maze datasets
Exporting search results
Performance comparison between algorithms

# Author #

Eddie Nguyen

Bachelor's Programme in Computer Science and Engineering
University of Oulu, Finland
