# [CS 170] Eight-Puzzle-Project
Project 1: Solve the Eight Puzzle Problem

Problem: 

The Eight Puzzle consists of a 3x3 board with 8 numbered tiles and one blank space. The goal is to move the tiles around until the blank space in the bottom-right corner.


Approach 1: 

We will be using the Uniform Cost Search method.

1) Uniform Cost Search Overview

- Uniform Cost Search expands the node with the lowest path cost g(n) at each step.
- It is essentially a breadth-first search that uses a priority queue to find the least expensive path.
    - We will keep a closed list of expanded nodes to avoid revisiting the same state.

2) Cost Function

- g(n): the actual cost from the start node to any node n. 
    - This can be considered as the number of moves made from the initial state to reach the current state.
- h(n): hardcoded to zero because Uniform Cost Search does not use heuristic function.
- f(n) = g(n): It represents the estimated total cost of the cheapest solution through n.

3) Algorithm

- Initialize the priority open list with the initial state of the puzzle, with a path cost of 0.
- Loop until the open list is empty:
    - Remove the node with the lowest g(n) from the open list.
    - Generate all its successors by moving the blank space up, down, left, or right.
    - For each successor:
        - Calculate g(n) for the successor as the parent's g(n) plus the cost of the move (1 for each move in our case).
        - If it is the goal, stop and return the solution by tracing the path back to the initial state.
        - Check if the new state has already be seen before with a higher cost in the priority queue. 
            - If so, update its cost and position in the queue.
            - if not, add it to the queue.
- Return Fail if no solution is found after the open list is empty.

Approach 2: 

We will be using the A* with the Misplaced Tile heuristic method.

1) A* with Misplaced Tile Heuristic Overview

- A* algorithm is a search algorithm used to find the shortest path from start node to a target node

2)  Cost Function

- g(n): Cost from start state to current state
- h(n): The heuristic that estimates the lowest required amount of moves to reach the goal.
      - h(n): Count the number of misplaced tiles from the initial state against the goal state
- f(n) = g(n) + h(n): The cost function that A* minimizes. IT represents the estimated total cost of the cheapest solution through n.

3) Choosing the Heuristic [h(n)]

- To compute the misplaced tile heuristic for puzzles like the 8-puzzle, count the number of tiles that are not in their goal position, excluding the blank tile. 
    - This heuristic value represents the minimum number of tiles that need to be moved to reach the goal state
    - It is used to estimate the distance from the current state to the solution in search algorithms.

4) Algorithm
  
- Initialize the open list (priority queue) with the initial state of the puzzle.
- Loop until the open list is empty:
    - Remove the node with the lowest f(n) from the open list.
    - Generate all its successors by moving the blank space up, down, left, or right
    - For each successor:
        - Compute g, h, and f (cost functions)
        - If it is the goal, stop and return the solution by tracing the path back to the initial state.
        - If a node with the same position as successor is in the open list with lower f, skip this successor.
        - Otherwise, add the successor to the open list.
- Return None if no solution is found after the open list is empty.


Approach 3: 

We will be using the A* with the Euclidean Distance heuristic method.

1) A* with the Euclidean Distance heuristic method overview

- A* algorithm is a search algorithm that is used to find the shortest path from a start node to a target node

2) Cost Function

- g(n): the actual cost from the start node to any node n.
- h(n): a heuristic that estimates the cost of the cheapest path from n to the goal. 
    - h(n) = sqrt[(x2​−x1​)^2 + (y2​−y1​)^2​]
- f(n) = g(n) + h(n): the cost function that A* minimizes. It represents the estimated total cost of the cheapest solution through n.

3) Choosing the Heuristic [h(n)]

- The heuristic function estimates the minimum cost from the current state to the goal state. 
- The Euclidean Distance heuristic measures the straight-line distance between each tile’s current position and its goal position, summing these distances across all tiles. It's calculated as follows:
    - h(n) = sqrt[(x2​−x1​)^2 + (y2​−y1​)^2​]
        - (x1, y1) is the current position of a tile, and (x2, y2) is the position in the goal state.

4) Algorithm

- Initialize the open list (priority queue) with the initial state of the puzzle.
- Loop until the open list is empty:
    - Remove the node with the lowest f(n) from the open list.
    - Generate all its successors by moving the blank space up, down, left, or right
    - For each successor:
        - Compute g, h, and f (cost functions)
        - If it is the goal, stop and return the solution by tracing the path back to the initial state.
        - If a node with the same position as successor is in the open list with lower f, skip this successor.
        - Otherwise, add the successor to the open list.
- Return None if no solution is found after the open list is empty.

Optimization 

- Keep a closed list of expanded nodes to avoid revisiting the same state. 
    - We add each explored node to a list and check this list each time we want to add a node to the open list.
    - Keep track of the costs of the states to prevent revisiting a state that was previously encountered with a higher cost.

Conclusion

In this project, we explored three different heuristic methods—Uniform Cost Search, Misplaced Tile, and Euclidean Distance to solve the 8-puzzle problem. Each method utilizes a different heuristic to estimate the cost from the current state to the goal state, with Uniform Cost Search considering only the cost without any heuristic. This approach allowed us to systematically compare the effectiveness and efficiency of each heuristic in guiding the A* search towards the solution. For relatively simple puzzles, the choice of heuristic shows minimal impact; however, as puzzles increase in complexity, the effectiveness of a heuristic becomes more pronounced, demonstrating that a good heuristic significantly enhances search efficiency compared to a weak or nonexistent heuristic.



















