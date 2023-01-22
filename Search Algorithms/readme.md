# A1 - Search

###### Made by Sri Varsha Chellapilla (srchell),  Roopank Kohli (rookohli) and Akash Bhapkar (abhapkar) 

## Part 1

### Description of A* Search Algorithm:

A* search algorithm is best-first search which computes cost of states by adding 

_g(n): the cost of getting to the current state, and_

_h(n): the cost of getting from the current state to the goal state_

The cost function function f(n) is computed as:
f(n) = g(n) + h(n)

Here h(n) is the admissible heuristic function, an admissible heuristic is a heuristic that never overestimates the cost to reach a goal state.

### Solution Overview:

To solve the 2021 puzzle using A* algorithm the abstraction is as below 

**Abstraction:**

- State Space So: All the possible board configurations
- Initial State S: The input intial board
- Successor function: All the valid moves that can be made, the valid moves for 2021 puzzle would be (L1, L2, L3, L4, L5, R1, R2, R3, R4, R5, U1, U2, U3, U4, U5, D1, D2, D3, D4, D5, Oc, Occ, Ic, Icc). The suucessor move would be the from the list of valid moves that has least cost.
- Goal State: Board configuration with 1 to 25 tiles in sequence. 
- Cost function: The cost function f(n) would br determined as: f(n) = g(n) + h(n)
  - here g(n) is the cost from my intial state to my current state.
  - h(n) is the admissible heuristic function which gives the minimum cost to reach from my current state to my goal state.

### Difficulties:
As both manhattan distance and No. of misplaced tiles are not admissible heuristics because of the valid moves, it was challenging to come up with a combination of a heuristic that does not overestimate the cost.

The heuristic used calulates the cost from current state to goal state as below:
- After checking all the successor function and if the cost is less than or equal to 2 that is the goal state can be reached by <= 2 moves the manhattan distance is being used;|X1 - X2| + |Y1 - Y2|.
- If the total number of moves required to reach goal state is >2 the manhattan distance heuristic is over estimating the cost because with rotation the No. of moves to reach the goal would be less. In this case, The row_cost and col_cost are being calucated as (len(board) - row) and (len(board[0] - col). Total cost calculated as adding row_cost and col_cost while dividing the cost by 5(if moving L, R, U, D) or 16(Oc, Occ) or 8(Ic, Icc) to make the cost admissible. We have used 3-d manhattan distance to make it admissible.

1. In this problem, what is the branching factor of the search tree?

The branching factor of the search tree is 24.

2. If the solution can be reached in 7 moves, about how many states would we need to explore before we
found it if we used BFS instead of A* search? A rough answer is fine.

The states that would be explored before we found the solution would be:
24^6 + 24^5 + 24^4 + 24^3 + 24^2 + 24^1 + 24^0


## Part 2

Here, we were provided with the following :

* road-segments.txt - a dataset of major highway segments of the United States (and parts of southern Canada and 
northern Mexico), including highway names, distances, and speed limits.

* city-gps.txt - a dataset of cities and towns with corresponding latitude-longitude positions.
* route.py - it contained the skeleton code where we are supposed to publish our solution.

### Problem Statement

To complete the get_route() function, which returns the best route according to the specified cost function, as well as 
the number of segments, number of miles, number of hours for a car driver, and expected number of hours for the delivery
driver.

### Solution

The solution comprises the implementation of the code route.py. The problem was addressed with the A* search algorithm.
A* algorithm is a form of Best First Search algorithm which computes the cost using the following formula :

f(s) = g(s)+h(s)

where g(s) is the cost of the best path found so far to s and h(s) is an admissible heuristic which never overestimates 
the cost.


### Abstractions

Based upon the problem given, these are the following abstractions:

State Space - It is the collection of all cities/nodes which are available in the driver's universe. All the nodes for
which the coordinates (latitude and longitude) are provided to us, can be considered as the state space in this problem.

Initial State - The initial-city or the starting city in this problem is our initial state

Goal State - It is the final state or in this case the final destination city where the driver is supposed to reach from
the initial state.

Successor Function - Successor Function is nothing but a function which provides the user with the next successive 
states. In this case, if we are providing an input city to the successor function, then the adjacent cities connected 
to our input are the successors. This can be computed by logically traversing the road-segments.txt file. 

Cost Function - The cost function f(s) consists of two parts, g(s) and h(s). g(s) is the optimal cost (distance covered,
time taken, segments traversed, and delivery time taken) computed from the source state to the next successive state 
(computed with successor function). h(s) is estimated admissible cost computed that provides us with the best result.

### Design Decisions

A number of data structures including list, tuple, dictionary, heapq etc. and a variety of inbuilt functions like 
math.sqrt, math.tanh, sorted were used in this solution. The main approach followed here is to compute the successors or
successive cities of our source node and this is implemented using a dictionary. From that dictionary, the most optimal 
successor is selected and this optimality is decided using the cost function provided by the user. This cost function 
can be distance travelled, the shortest time, delivery time or segments traversed. The heapq is used to maintain the 
fringe and pop out the suitable and most optimal successor based on the priority. 

### Problems Faced

Several problems were encountered while designing the optimal solution to the given problem. These are mentioned below : 

* Initially the solution was implemented using the priority queue, but it was observed that it was taking a lot of time 
to compute the solution. Later on, it was implemented using the heapq which is nothing but a heap implementation of a 
priority queue. The main advantage with heapq is that it provides us with the smallest element in the least amount of 
time which was O(log(n)).

* It was difficult to compute a cost function for the calculation of segments.



## Part 3

### Approach:
For this problem it was clear that local search needed to be used because of the problem statement. My approach was first of all make all the minumum number of teams as possible and return it quickly. 
Then make teams by checking the non-preferred users for each user and then form a team. And lastly I combined these two conditions and started looking for the solution with minimum cost.

### Abstractions:

**State Space** : All the possible combinations of teams given users list

**Initial State** : Initial assignment of teams

**Goal State** : Local minimum cost within reasonable amount of time

**Successor Function** : randomly picked team with less cost than previous

**Cost Function** : Cost of team arrangements based on conditions

### Solution:
The solution I implemented makes a quick team first and yield it with the cost. 
Next time it tries to minimize the cost of the team by not putting non-preferred people in one team.
And for the last while loop, I am checking the random teams with cost less than the previous solutions and yielding them.


### Design Decisions:
Since every person has preferrences and we need to iterate over all the persons in each group, while reading the file I stored the input in dictionary which helped me use it efficiently on later stages of the program.

### Problem Faced:
First I tried to create teams using itertools but the team combinations were exceeding the memory for list.
Therefore I tried using random module and it was working as expected.

