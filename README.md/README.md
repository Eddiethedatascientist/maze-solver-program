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


