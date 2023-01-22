#!/usr/local/bin/python3
# solver2021.py : 2021 Sliding tile puzzle solver
#
# Code by: Sri Varsha Chellapilla (srchell),  Roopank Kohli (rookohli) and Akash Bhapkar (abhapkar)
#


import sys
import numpy as np
import copy
import heapq
import time

ROWS = 5
COLS = 5

def shift_left(board, row_number):
    output_board = board[row_number]
    temp = output_board[0]
    for i in range(0, len(output_board) - 1):
        output_board[i] = output_board[i + 1]
    output_board[-1] = temp
    board[row_number] = output_board
    return board


def shift_right(board, row_number):
    output_board = board[row_number]
    temp = output_board[-1]
    for i in range(len(output_board) - 1, -1, -1):
        output_board[i] = output_board[i - 1]
    output_board[0] = temp
    board[row_number] = output_board
    return board


def shift_up(board, col_number):
    temp = board[0][col_number]
    for i in range(0, ROWS - 1):
        board[i][col_number] = board[i + 1][col_number]
    board[ROWS - 1][col_number] = temp
    return board


def shift_down(board, col_number):
    temp = board[ROWS - 1][col_number]
    for i in range(ROWS - 1, 0, -1):
        board[i][col_number] = board[i - 1][col_number]
    board[0][col_number] = temp
    return board


def rotate_outer_clockwise(board, begin_row, begin_col, end_row, end_col):
    temp1 = board[begin_row][end_col]
    for i in range(end_col, begin_col, -1):
        board[begin_row][i] = board[begin_row][i - 1]

    temp2 = board[end_row][end_col]
    for i in range(end_row, begin_row + 1, -1):
        board[i][end_col] = board[i - 1][end_col]

    temp3 = board[end_row][begin_col]
    for i in range(begin_col, end_col - 1):
        board[end_row][i] = board[end_row][i + 1]

    for i in range(begin_row, end_row - 1):
        board[i][begin_col] = board[i + 1][begin_col]

    board[begin_row + 1][end_col] = temp1
    board[end_row][end_col - 1] = temp2
    board[end_row - 1][begin_col] = temp3

    return board


def rotate_outer_counter_clockwise(board, begin_row, begin_col, end_row, end_col):
    temp1 = board[begin_row][begin_col]
    for i in range(begin_col, end_col):
        board[begin_row][i] = board[begin_row][i + 1]
    temp2 = board[end_row][begin_col]
    for i in range(end_row, begin_row + 1, -1):
        board[i][begin_col] = board[i - 1][begin_col]
    temp3 = board[end_row][end_col]
    for i in range(end_col, begin_col + 1, -1):
        board[end_row][i] = board[end_row][i - 1]
    for i in range(begin_row, end_row - 1):
        board[i][end_col] = board[i + 1][end_col]

    board[begin_row + 1][begin_col] = temp1
    board[end_row][begin_col + 1] = temp2
    board[end_row - 1][end_col] = temp3

    return board


def rotate_inner_clockwise(board, begin_row, begin_col, end_row, end_col):
    rotate_outer_clockwise(board, begin_row, begin_col, end_row, end_col)
    return board


def rotate_inner_counter_clockwise(board, begin_row, begin_col, end_row, end_col):
    rotate_outer_counter_clockwise(board, begin_row, begin_col, end_row, end_col)
    return board

def printable_board(board):
    return [ ('%3d ') * COLS % board[j:(j+COLS)] for j in range(0, ROWS*COLS, COLS)]


# return a list of possible successor states
def successors(state1):
    successor = []
    if len(state1) > 4:
        state = copy.deepcopy(state1)
        path = ""
        cost = 0
    else:
        state = copy.deepcopy(state1[3])
        path = copy.deepcopy(state1[1])
        cost = copy.deepcopy(state1[2])

    for i in range(len(state)):
        l = copy.deepcopy(shift_left(state, i))
        mvl = path + " L" + str(i+1)
        successor.append([l, mvl, cost+1])
        shift_right(state, i)
        del l

        r = copy.deepcopy(shift_right(state, i))
        mvr = path + " R"+str(i+1)
        successor.append([r, mvr, cost+1])
        shift_left(state, i)
        del r

        u = copy.deepcopy(shift_up(state, i))
        mvu = path + " U"+str(i+1)
        successor.append([u, mvu, cost+1])
        shift_down(state, i)
        del u

        d = copy.deepcopy(shift_down(state, i))
        mvd = path + " D"+str(i+1)
        successor.append([d, mvd, cost+1])
        shift_up(state, i)
        del d

    oc = copy.deepcopy(rotate_outer_clockwise(state, 0, 0, 4, 4))
    mvOc = path + " Oc"
    successor.append([oc, mvOc, cost+1])
    rotate_outer_counter_clockwise(state, 0, 0, 4, 4)
    del oc

    Occ = copy.deepcopy(rotate_outer_counter_clockwise(state, 0, 0, 4, 4))
    mvOcc = path + " Occ"
    successor.append([Occ, mvOcc, cost+1])
    rotate_outer_clockwise(state, 0, 0, 4, 4)
    del Occ

    Ic = copy.deepcopy(rotate_inner_clockwise(state, 1, 1, 3, 3))
    mvic = path + " Ic"
    successor.append([Ic, mvic, cost+1])
    rotate_inner_counter_clockwise(state, 1, 1, 3, 3)
    del Ic

    Icc = copy.deepcopy(rotate_inner_counter_clockwise(state, 1, 1, 3, 3))
    mvicc = path + " Icc"
    successor.append([Icc, mvicc, cost+1])
    rotate_inner_clockwise(state, 1, 1, 3, 3)
    del Icc

    return successor

def compute_cost(state, path):
    cost = 0
    goal_dict = { 1:[0,0], 2:[0,1], 3:[0, 2], 4:[0, 3], 5:[0,4],
                  6:[1,0], 7:[1,1], 8:[1, 2], 9:[1, 3], 10:[1,4],
                  11:[2,0], 12:[2,1], 13:[2,2], 14:[2,3], 15:[2,4],
                  16:[3,0], 17:[3,1], 18:[3,2], 19:[3,3], 20:[3,4],
                  21:[4,0], 22:[4,1], 23:[4,2], 24:[4,3], 25:[4,4]}
    move = path.split()[-1] if len(path) > 1 else ""

    for i in range(len(state)):
        for j in range(len(state[0])):
            val = state[i][j]
            g_row, g_col = goal_dict[val]
            row_cost, col_cost = 0, 0

            if abs(g_row - i) <= 2:
                row_cost = abs(g_row - i)
            else:
                row_cost = len(state) - abs(g_row - i)

            if abs(g_col - j) <= 2:
                col_cost = abs(g_col - j)
            else:
                col_cost = len(state[0]) - abs(g_col - j)

            cost += row_cost + col_cost

    #modified manhattan distance
    if move == 'Oc' or move == 'Occ':
        cost /= 16
    elif move == 'Icc' or move == 'Ic':
        cost /= 8
    else:
        cost /= 5

    return cost

# check if we've reached the goal
def is_goal(state):
    goal_state = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    if state == goal_state:
        return True
    return False

def solve(initial_board):
    """
    1. This function should return the solution as instructed in assignment, consisting of a list of moves like ["R2","D2","U1"].
    2. Do not add any extra parameters to the solve() function, or it will break our grading and testing code.
       For testing we will call this function with single argument(initial_board) and it should return 
       the solution.
    3. Please do not use any global variables, as it may cause the testing code to fail.
    4. You can assume that all test cases will be solvable.
    5. The current code just returns a dummy solution.
    """
    a = np.array(initial_board)
    b = a.reshape([5, 5])
    board = b.tolist()
    fringe = []
    _val = (compute_cost(board, ""), "", 0, board)
    heapq.heappush(fringe, _val)
    del _val
    visited = []
    visited.append(board)
    #i = 0
    while fringe:
        state = heapq.heappop(fringe)
        #print(state[0])
        #print(len(fringe))
        # i += 1
        #if i > 20: break

        if is_goal(state[3]):
            path = state[1].split()
            return path
        for succ in successors(state):
            if is_goal(succ[0]):
                path = succ[1].split()
                return path
            else:
                if succ[0] not in visited:
                    _val = (compute_cost(succ[0], succ[1])+succ[2], succ[1], succ[2], succ[0])
                    heapq.heappush(fringe, _val)
                    visited.append(succ[0])
                    del _val

    return []

# Please don't modify anything below this line
#
if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise(Exception("Error: expected a board filename"))

    start_state = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            start_state += [ int(i) for i in line.split() ]

    if len(start_state) != ROWS*COLS:
        raise(Exception("Error: couldn't parse start state file"))
    print(tuple(start_state))
    print("Start state: \n" +"\n".join(printable_board(tuple(start_state))))
    #st_time = time.time()
    print("Solving...")
    route = solve(tuple(start_state))
    
    print("Solution found in " + str(len(route)) + " moves:" + "\n" + " ".join(route))
    #print("time: ", time.time() - st_time)
