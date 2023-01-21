## 1.	ROUTE PICHU:

## Overview of the solution:
To find the path between Pichu ‘p’ and Agent ‘@’ BFS search technique has been used in which the priority queue pops out the least priority state from the FRINGE.
After poping out the node its successor nodes are stored in the fring to traverse. BFS 

## Abstraction:

State Space:  The state space for the path finding maze would be all the dots ‘.’ other than the walls ‘X’. That is the states where Pichu can move.

Initial state: Pichu ‘p’ in the start position.

Successor Function: Move Pichu to a valid state. Pichu cannot be moved if there is an obstacle ‘X’.

Goal State: Pichu ‘P’ and Agent ‘@’ at same location.

Cost Function: Irrrelevant. The cost function will be uniform when using BFS.

## Difficulties:

Initially the code was taking a long time to execute and give output as the visited nodes were being revisited. To reduce the output time the condition “if move[0] not in visited:” was added which prevents visiting same nodes multiple times.
 

## 2.	ARRANGE_PICHU:

## Overview of the solution:
To arrange k pichus on the given map BFS search technique is use. 

## Abstraction:

State Space: The total number of possible positions where k pichu can be placed over the given map with walls.

Initial state: No or ‘x’ number of pichus on the given map.

Success Function: Placing pichu in a valid state so that no pichu can see other from horizontal, vertical or diagonal directions.

Goal state: k pichus on the map with no conflicts.

Cost Function: Irrelevant.

## Difficulties:
I have tried checking the diagonal conflict using abs difference between pichu, walls and its next move. I have encountered difficultiy in row and column increment and decrement due to which the difference value even though it was 1 the pichus were being placed diagonally.
I have then defined 4 different functions to check to check left upper and left lower, right upper and right lower diagonals seperately using while loop but taking a center point and incrementing and crementing the row and column values.

When the K value is more than 6 for map1.txt, the pichus are not being place and "NoneType object" error is being returned and for map2 if the k value is more than 5 "NoneType object" error is being returned. The NoneType error is usually raised when none is being returned. I have not understood wht in this case it is being returned.



