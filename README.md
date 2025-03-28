# Snake Game-Themed AI Case Study: Depth-Limited Search for Food Collection
## Output:
https://github.com/user-attachments/assets/2b79659d-80f8-4bcc-bff0-c569390717d7
## Question
### How can Depth-Limited Search (DLS) be applied in the Snake Game to efficiently collect food within a limited number of moves while avoiding collisions?

## Introduction
### The Snake Game is a classic arcade game where a snake navigates a grid to collect food while avoiding collisions with itself and the walls. As the snake grows longer, maneuverability becomes more challenging. This case study explores how Depth-Limited Search (DLS) can be applied to maximize food collection within a constrained number of moves.

## Case Study Overview
### This study focuses on implementing an AI strategy using DLS to efficiently navigate the grid, collect food, and avoid obstacles within a predefined move limit. The study also explores enhancements like dynamic timers that reduce available moves after each food collection.

## Objectives
- **Implement Depth-Limited Search (DLS)** for pathfinding in the Snake Game.
- **Ensure the AI efficiently collects food** while adhering to the move limit.
- **Address challenges** such as balancing speed and collision avoidance.
- **Analyze DLS performance** across different grid configurations.
- **Explore extensions** like dynamic move constraints.

## Tasks and Solutions
### Task Explanation
- The AI must strategically navigate the grid to collect food within a set move limit while avoiding collisions.

### PEAS Description
- **Performance Measure:** Maximize food collection within the move limit while avoiding collisions.
- **Environment:** A 2D grid representing the game board with food, walls, and the snake.
- **Actuators:** Snake's movement (up, down, left, right).
- **Sensors:** Grid state information (food locations, obstacles, remaining moves).

### Task Environment Properties
- **Fully Observable:** The entire grid state is known.
- **Dynamic:** The environment updates as the snake moves and grows.
- **Discrete:** The grid consists of distinct cells with fixed positions.
- **Deterministic:** Each move has a predictable outcome.

## Problem Formulation
- **State:** Snake position, length, food locations, and remaining moves.
- **Initial State:** Snake starts at a predefined position with a set move limit.
- **Actions:** Move in one of four directions.
- **Transition Model:** The snake moves, updating its state.
- **Goal Test:** Maximize food collection within the move limit without collisions.
- **Path Cost:** Each move has a cost; collecting food provides a benefit.

## Algorithm: Depth-Limited Search (DLS)
### DLS is a variation of Depth-First Search (DFS) that imposes a search depth limit to prevent excessive exploration. This is beneficial in the Snake Game, where move constraints exist.

## Algorithm Utilization
1. **The snake identifies food locations** from its starting position.
2. **DLS explores possible paths** within a predefined depth limit.
3. **The algorithm prioritizes paths** leading to food.
4. **If a path reaches food within the limit,** the snake follows that path.
5. **The process repeats** until the move limit is reached.
6. **A dynamic move constraint** can be introduced to reduce available moves after each food collection, increasing difficulty.

---
### This study demonstrates how DLS can be applied to pathfinding in a constrained environment and explores possible extensions to enhance gameplay complexity.

