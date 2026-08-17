## Maze Solver & Algorithm Solver and Visualization Tool ##

A Python application for loading, visualizing, and solving maze problems using multiple pathfinding algorithms. The application provides a graphical user interface for selecting maze data, choosing a search algorithm, running the solver, and displaying the resulting path and performance metrics.

Project Overview

This project was developed as part of the Elementary Programming course at the University of Oulu.

The objective of the project is to build a maze-solving application that allows users to experiment with and compare different pathfinding algorithms through a single graphical interface.

The application supports four pathfinding algorithms, implemented from scratch:

A* Search
Greedy Search
Breadth-First Search (BFS)
Depth-First Search (DFS)

Maze data is stored externally as .txt files and can be loaded into the application. The selected algorithm processes the maze and returns the discovered route together with information about the search process and execution performance.

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
Supported Algorithms
A* Search

A* Search combines the cost of reaching a node with a heuristic estimate of the remaining distance to the goal.

The implementation uses separate modules for the main algorithm and supporting operations such as routing, point handling, and path reconstruction.

Greedy Search

Greedy Search selects the most promising available position based on its estimated distance to the goal.

The implementation ranks valid moves according to their heuristic distance and continuously selects the most promising candidate.

Breadth-First Search (BFS)

BFS explores the maze level by level.

The implementation maintains visited positions, possible paths, search levels, and route records until the destination is reached.

Depth-First Search (DFS)

DFS explores one path as deeply as possible before backtracking and continuing with another available path.

The implementation maintains the explored positions and reconstructs the successful route once the destination is reached.
