# New York Times Digits Solver

## Description

This is a solver for the New York Times Digits puzzle. The goal of the game is to combine 6 numbers through addition, subtraction, multiplication, and division into one target number. The game is available on the [New York Times website](https://www.nytimes.com/games/digits).

This solver finds all solutions and determines the shortest solution.

Enter the puzzle information at the top of the script:

```python
input = [5,7,9,11,13,23]
target = 463
```

The output from the progam for the above case is:
```
--------------------------------------------------------
Input: [5, 7, 9, 11, 13, 23]
Target: 463
--------------------------------------------------------
First solution found:
[(7, '+', 5), (23, '+', 11), (12, '+', 9), (34, '*', 13), (442, '+', 21)]
--------------------------------------------------------
Execution time: 0.64 seconds
Number of solutions found: 194
Shortest solution:
[(9, '+', 5), (23, '+', 11), (34, '*', 14), (476, '-', 13)]
```

For the above case, this means that the shortest solution is:
```
9 + 5 = 14
23 + 11 = 34
34 * 14 = 476
476 - 13 = 463
```