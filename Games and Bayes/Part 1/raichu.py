#
# raichu.py : Play the game of Raichu
#
# PLEASE PUT YOUR NAMES AND USER IDS HERE!
#
# Based on skeleton code by D. Crandall, Oct 2021
#
import sys
import time
import copy

def board_to_string(board, N):
    return "\n".join(board[i:i+N] for i in range(0, len(board), N))


def find_best_move(board, N, player, timelimit):
    # This sample code just returns the same board over and over again (which
    # isn't a valid move anyway.) Replace this with your code!
    #
    b = []
    k = 0
    #make board into list of lists
    for i in range(N):
        r = []
        for j in range(N):
            r.append(board[k])
            k += 1
        b.append(r)
    board=b.copy()#np.reshape(np.array([(j) for j in board] ),((int(math.sqrt(len(board))),int(math.sqrt(len(board))) )))
    ans=""
    for t in alphabeta(board,-99999,99999,player,len(board)):
        for k in t:
            for l in k:
               ans+=str(l)
    return ans
    #while True:
     #   time.sleep(1)
      #  yield ans
        
def valid_index(pos, n, m):
    return 0 <= pos[0] < n and 0 <= pos[1] < m

def pichu_moves(b, N, player):
    moves = []
    if player == 'w':
        for i, row in enumerate(b):
            for j, ele in enumerate(row):
                if ele == player:
                    temp = copy.deepcopy(b)
                    #left diagonal down
                    if valid_index([i+1,j-1], N, N):
                        if temp[i+1][j-1] == '.':
                            temp[i + 1][j - 1] = player
                            temp[i][j] = '.'
                            if i+1 == N-1:
                                temp[i + 1][j - 1] = '@'
                            #print(temp)
                            moves.append(copy.deepcopy(temp))
                        elif temp[i+1][j-1] == 'b':
                            if valid_index([i + 2, j - 2], N, N):
                                if temp[i+2][j-2] == '.':
                                    temp[i + 2][j - 2] = player
                                    temp[i+1][j-1] = '.'
                                    temp[i][j] = '.'
                                    if i + 2 == N - 1:
                                        temp[i + 2][j - 2] = '@'  #create raichu
                                    #print(temp)
                                    moves.append(copy.deepcopy(temp))
                    #right diagonal down
                    temp = copy.deepcopy(b)
                    if valid_index([i+1, j+1], N, N):
                        if temp[i+1][j+1] == '.':
                            temp[i + 1][j + 1] = player
                            temp[i][j] = '.'
                            if i+1 == N-1:
                                temp[i + 1][j + 1] = '@'
                            #print(temp)
                            moves.append(copy.deepcopy(temp))
                        elif temp[i+1][j+1] == 'b':
                            if valid_index([i + 2, j + 2], N, N):
                                if temp[i+2][j+2] == '.':
                                    temp[i + 2][j + 2] = player
                                    temp[i+1][j+1] = '.'
                                    temp[i][j] = '.'
                                    if i + 2 == N - 1:
                                        temp[i + 2][j + 2] = '@'  #create raichu
                                    #print(temp)
                                    moves.append(copy.deepcopy(temp))
    elif player == 'b':
        for i, row in enumerate(b):
            for j, ele in enumerate(row):
                if ele == player:
                    temp = copy.deepcopy(b)
                    #left diagonal up
                    if valid_index([i-1, j-1], N, N):
                        if temp[i-1][j-1] == '.':
                            temp[i - 1][j - 1] = player
                            temp[i][j] = '.'
                            if i-1 == 0:
                                temp[i - 1][j - 1] = '$' # create black raichu
                            #print(temp)
                            moves.append(copy.deepcopy(temp))
                        elif temp[i-1][j-1] == 'w':
                            if valid_index([i-2,j-2], N, N):
                                if temp[i-2][j-2] == '.':
                                    temp[i - 2][j - 2] = player
                                    temp[i-1][j-1] = '.'
                                    temp[i][j] = '.'
                                    if i - 2 == 0:
                                        temp[i - 2][j - 2] = '$'  # create black raichu
                                    #print(temp)
                                    moves.append(copy.deepcopy(temp))
                    #right diagonal up
                    temp = copy.deepcopy(b)
                    if valid_index([i-1,j+1], N, N):
                        if temp[i-1][j+1] == '.':
                            temp[i - 1][j + 1] = player
                            temp[i][j] = '.'
                            if i-1 == 0:
                                temp[i - 1][j + 1] = '$'
                            #print(temp)
                            moves.append(copy.deepcopy(temp))
                        temp = copy.deepcopy(b)
                        if temp[i-1][j+1] == 'w':
                            if valid_index([i - 2, j + 2], N, N):
                                if temp[i-2][j+2] == '.':
                                    temp[i - 2][j + 2] = player
                                    temp[i-1][j+1] = '.'
                                    temp[i][j] = '.'
                                    if i - 2 == 0:
                                        temp[i - 2][j + 2] = '$'  #create raichu
                                    #print(temp)
                                    moves.append(copy.deepcopy(temp))
    return moves
def pikachu_moves(b, N, player):
    #print("abjahdv")
    moves = []
    if player == 'W':
        #print("bidcbkfji")
        for i, row in enumerate(b):
            for j, ele in enumerate(row):
                if ele == player:
                    temp = copy.deepcopy(b)
                    #forward 1 step
                    if valid_index([i + 1, j], N, N):
                        if temp[i+1][j] == '.':
                            temp[i + 1][j] = player
                            temp[i][j] = '.'
                            if i+1 == N-1:
                                temp[i + 1][j] = '@'
                            #print(temp)
                            moves.append(copy.deepcopy(temp))
                            #forward 2 steps
                            temp = copy.deepcopy(b)
                            if valid_index([i+2, j], N, N):
                                if temp[i+2][j] == ".":
                                    temp[i+2][j] = player
                                    temp[i][j] = "."
                                    if i+2 == N-1:
                                        temp[i + 2][j] = '@'
                                    #print(temp)
                                    moves.append(copy.deepcopy(temp))
                            #jump over a pichu/pikachu of black player in forward direction 3 steps
                            temp = copy.deepcopy(b)
                            if valid_index([i+2, j], N, N):
                                if temp[i+2][j] == "b" or temp[i+2][j] == "B":
                                    if valid_index([i+3, j], N, N):
                                        if temp[i+3][j] == ".":
                                            temp[i+3][j] = player
                                            temp[i+2][j] = "."
                                            temp[i][j] = "."
                                            if i+3 == N-1:
                                                temp[i+3][j] = "@"
                                            #print(temp)
                                            moves.append(copy.deepcopy(temp))
                        # jump over a pichu/pikachu of black player in forward direction 2 step
                        temp = copy.deepcopy(b)
                        if temp[i+1][j] == 'b' or temp[i+1][j] == "B":
                            if valid_index([i+2, j], N, N):
                                if temp[i+2][j] == ".":
                                    temp[i+2][j] = player
                                    temp[i+1][j] = "."
                                    temp[i][j] = "."
                                    if i+2 == N-1:
                                        temp[i + 2][j] = '@'
                                        #print(temp)
                                    moves.append(copy.deepcopy(temp))
                                    #jump over a pichu/pikachu of black player in forward direction 3 steps
                                    temp = copy.deepcopy(b)
                                    if valid_index([i+3, j], N, N):
                                        temp = copy.deepcopy(b)
                                        if temp[i+3][j] == ".":
                                            temp[i+3][j] = player
                                            temp[i+1][j] = "."
                                            temp[i][j] = "."
                                            if i+3 == N-1:
                                                temp[i+3][j] = "@"
                                            #print(temp)
                                            moves.append(copy.deepcopy(temp))
                    temp = copy.deepcopy(b)
                    if valid_index([i, j+1], N, N):
                        if temp[i][j+1] == '.':
                            temp[i][j+1] = player
                            temp[i][j] = '.'
                            moves.append(copy.deepcopy(temp))
                            # left 2 steps
                            temp = copy.deepcopy(b)
                            if valid_index([i, j+2], N, N):
                                if temp[i][j+2] == ".":
                                    temp[i][j+2] = player
                                    temp[i][j] = "."
                                    moves.append(copy.deepcopy(temp))
                            # jump over a pichu/pikachu of black player in left direction 3 steps
                            temp = copy.deepcopy(b)
                            if valid_index([i, j+2], N, N):
                                if temp[i][j+2] == "b" or temp[i][j+2] == "B":
                                    if valid_index([i, j+3], N, N):
                                        if temp[i][j+3] == ".":
                                            temp[i][j+3] = player
                                            temp[i][j+2] = "."
                                            temp[i][j] = "."
                                            moves.append(copy.deepcopy(temp))
                        # jump over a pichu/pikachu of black player in left direction 2 step
                        temp = copy.deepcopy(b)
                        if temp[i][j+1] == 'b' or temp[i][j+1] == "B":
                            if valid_index([i, j+2], N, N):
                                if temp[i][j+2] == ".":
                                    temp[i][j+2] = player
                                    temp[i][j+1] = "."
                                    temp[i][j] = "."
                                    moves.append(copy.deepcopy(temp))
                                    # jump over a pichu/pikachu of black player in left direction 3 steps
                                    if valid_index([i, j+3], N, N):
                                        temp = copy.deepcopy(b)
                                        if temp[i][j+3] == ".":
                                            temp[i][j+3] = player
                                            temp[i][j+1] = "."
                                            temp[i][j] = "."
                                            moves.append(copy.deepcopy(temp))
                    temp = copy.deepcopy(b)
                    if valid_index([i, j-1], N, N):
                        if temp[i][j-1] == '.':
                            temp[i][j-1] = player
                            temp[i][j] = '.'
                            moves.append(copy.deepcopy(temp))
                            # right 2 steps
                            temp = copy.deepcopy(b)
                            if valid_index([i, j-2], N, N):
                                if temp[i][j-2] == ".":
                                    temp[i][j-2] = player
                                    temp[i][j] = "."
                                    moves.append(copy.deepcopy(temp))
                            # jump over a pichu/pikachu of black player in right direction 3 steps
                            temp = copy.deepcopy(b)
                            if valid_index([i, j-2], N, N):
                                if temp[i][j-2] == "b" or temp[i][j-2] == "B":
                                    if valid_index([i, j-3], N, N):
                                        if temp[i][j-3] == ".":
                                            temp[i][j-3] = player
                                            temp[i][j-2] = "."
                                            temp[i][j] = "."
                                            moves.append(copy.deepcopy(temp))
                        # jump over a pichu/pikachu of black player in left direction 2 step
                        temp = copy.deepcopy(b)
                        if temp[i][j-1] == 'b' or temp[i][j-1] == "B":
                            if valid_index([i, j-2], N, N):
                                if temp[i][j-2] == ".":
                                    temp[i][j-2] = player
                                    temp[i][j-1] = "."
                                    temp[i][j] = "."
                                    moves.append(copy.deepcopy(temp))
                                    # jump over a pichu/pikachu of black player in left direction 3 steps
                                    temp = copy.deepcopy(b)
                                    if valid_index([i, j-3], N, N):
                                        temp = copy.deepcopy(b)
                                        if temp[i][j-3] == ".":
                                            temp[i][j-3] = player
                                            temp[i][j-1] = "."
                                            temp[i][j] = "."
                                            moves.append(copy.deepcopy(temp))
    if player == 'B':
        for i, row in enumerate(b):
            for j, ele in enumerate(row):
                if ele == player:
                    temp = copy.deepcopy(b)
                    #forward 1 step
                    if valid_index([i - 1, j], N, N):
                        if temp[i-1][j] == '.':
                            temp[i - 1][j] = player
                            temp[i][j] = '.'
                            if i - 1 == 0:
                                temp[i - 1][j] = '$'
                            #print(temp)
                            moves.append(copy.deepcopy(temp))
                            #forward 2 steps
                            temp = copy.deepcopy(b)
                            if valid_index([i-2, j], N, N):
                                if temp[i-2][j] == ".":
                                    temp[i-2][j] = player
                                    temp[i][j] = "."
                                    if i-2 == 0:
                                        temp[i - 2][j] = '$'
                                    #print(temp)
                                    moves.append(copy.deepcopy(temp))
                            #jump over a pichu/pikachu of white player in forward direction 3 steps
                            temp = copy.deepcopy(b)
                            if valid_index([i-2, j], N, N):
                                if temp[i-2][j] == "w" or temp[i-2][j] == "W":
                                    if valid_index([i-3, j], N, N):
                                        if temp[i-3][j] == ".":
                                            temp[i-3][j] = player
                                            temp[i-2][j] = "."
                                            temp[i][j] = "."
                                            if i-3 == 0:
                                                temp[i-3][j] = "$"
                                            #print(temp)
                                            moves.append(copy.deepcopy(temp))
                        # jump over a pichu/pikachu of white player in forward direction 2 step
                        temp = copy.deepcopy(b)
                        if temp[i-1][j] == 'w' or temp[i-1][j] == "W":
                            if valid_index([i-2, j], N, N):
                                if temp[i-2][j] == ".":
                                    temp[i-2][j] = player
                                    temp[i-1][j] = "."
                                    temp[i][j] = "."
                                    if i-2 == 0:
                                        temp[i - 2][j] = '$'
                                        #print(temp)
                                    moves.append(copy.deepcopy(temp))
                                    #jump over a pichu/pikachu of white player in forward direction 3 steps
                                temp = copy.deepcopy(b)
                                if valid_index([i-3, j], N, N):
                                    temp = copy.deepcopy(b)
                                    if temp[i-3][j] == ".":
                                        temp[i-3][j] = player
                                        temp[i-1][j] = "."
                                        temp[i][j] = "."
                                        if i-3 == 0:
                                            temp[i-3][j] = "$"
                                            #print(temp)
                                        moves.append(copy.deepcopy(temp))
                    temp = copy.deepcopy(b)
                    if valid_index([i, j-1], N, N):
                        if temp[i][j-1] == '.':
                            temp[i][j-1] = player
                            temp[i][j] = '.'
                            moves.append(copy.deepcopy(temp))
                            # left 2 steps
                            temp = copy.deepcopy(b)
                            if valid_index([i, j-2], N, N):
                                if temp[i][j-2] == ".":
                                    temp[i][j-2] = player
                                    temp[i][j] = "."
                                    moves.append(copy.deepcopy(temp))
                            # jump over a pichu/pikachu of white player in left direction 3 steps
                            temp = copy.deepcopy(b)
                            if valid_index([i, j-2], N, N):
                                if temp[i][j-2] == "w" or temp[i][j-2] == "W":
                                    if valid_index([i, j-3], N, N):
                                        if temp[i][j-3] == ".":
                                            temp[i][j-3] = player
                                            temp[i][j-2] = "."
                                            temp[i][j] = "."
                                            moves.append(copy.deepcopy(temp))
                        # jump over a pichu/pikachu of white player in left direction 2 step
                        temp = copy.deepcopy(b)
                        if temp[i][j-1] == 'w' or temp[i][j-1] == "W":
                            if valid_index([i, j-2], N, N):
                                if temp[i][j-2] == ".":
                                    temp[i][j-2] = player
                                    temp[i][j-1] = "."
                                    temp[i][j] = "."
                                    moves.append(copy.deepcopy(temp))
                                    # jump over a pichu/pikachu of white player in left direction 3 steps
                                    temp = copy.deepcopy(b)
                                    if valid_index([i, j-3], N, N):
                                        temp = copy.deepcopy(b)
                                        if temp[i][j-3] == ".":
                                            temp[i][j-3] = player
                                            temp[i][j-1] = "."
                                            temp[i][j] = "."
                                            moves.append(copy.deepcopy(temp))

                    if valid_index([i, j+1], N, N):
                        if temp[i][j+1] == '.':
                            temp[i][j+1] = player
                            temp[i][j] = '.'
                            moves.append(copy.deepcopy(temp))
                            # right 2 steps
                            temp = copy.deepcopy(b)
                            if valid_index([i, j+2], N, N):
                                if temp[i][j+2] == ".":
                                    temp[i][j+2] = player
                                    temp[i][j] = "."
                                    moves.append(copy.deepcopy(temp))
                            # jump over a pichu/pikachu of white player in right direction 3 steps
                            temp = copy.deepcopy(b)
                            if valid_index([i, j+2], N, N):
                                if temp[i][j+2] == "w" or temp[i][j-2] == "W":
                                    if valid_index([i, j+3], N, N):
                                        if temp[i][j+3] == ".":
                                            temp[i][j+3] = player
                                            temp[i][j+2] = "."
                                            temp[i][j] = "."
                                            moves.append(copy.deepcopy(temp))
                        # jump over a pichu/pikachu of white player in left direction 2 step
                        temp = copy.deepcopy(b)
                        if temp[i][j+1] == 'w' or temp[i][j+1] == "W":
                            if valid_index([i, j+2], N, N):
                                if temp[i][j+2] == ".":
                                    temp[i][j+2] = player
                                    temp[i][j+1] = "."
                                    temp[i][j] = "."
                                    moves.append(copy.deepcopy(temp))
                                    # jump over a pichu/pikachu of white player in left direction 3 steps
                                    temp = copy.deepcopy(b)
                                    if valid_index([i, j+3], N, N):
                                        temp = copy.deepcopy(b)
                                        if temp[i][j+3] == ".":
                                            temp[i][j+3] = player
                                            temp[i][j+1] = "."
                                            temp[i][j] = "."
                                            moves.append(copy.deepcopy(temp))
    return moves

def raichu_moves(board, size, player):
    # To check left and right movement - "..b@B...W.W.W.W..w.w.w.w................b.b.b.b..B.B.B.B........"
    # player = "w"
    # player = "@"
    succList = []
    if player in ['w', 'W', '@']:
        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if value == "@":

                    # left side
                    for num in range(1, j + 1):
                        temp_board = copy.deepcopy(board)

                        if valid_index([i, j - num], N, N):
                            if temp_board[i][j - num] == '.':
                                temp_board[i][j - num] = '@'
                                temp_board[i][j] = '.'
                                succList.append(copy.deepcopy(temp_board))

                            elif temp_board[i][j - num] in 'bB$':
                                for index in range(1, j + 1):
                                    temp_board = copy.deepcopy(board)
                                    if valid_index([i, j - num - index], N, N):
                                        if temp_board[i][j - num - index] == '.':
                                            temp_board[i][j - num - index] = "@"
                                            temp_board[i][j - num] = '.'
                                            temp_board[i][j] = '.'
                                            succList.append(copy.deepcopy(temp_board))
                                        else:
                                            break
                                break
                            else:
                                break

                    # right side
                    for num in range(1, size - j):
                        temp_board = copy.deepcopy(board)

                        if valid_index([i, j + num], N, N):
                            if temp_board[i][j + num] == '.':
                                temp_board[i][j + num] = '@'
                                temp_board[i][j] = '.'
                                succList.append(copy.deepcopy(temp_board))

                            elif temp_board[i][j + num] in 'bB$':
                                for index in range(1, j + num):
                                    temp_board = copy.deepcopy(board)
                                    if valid_index([i, j + num + index], N, N):
                                        if temp_board[i][j + num + index] == '.':
                                            temp_board[i][j + num + index] = "@"
                                            temp_board[i][j + num] = '.'
                                            temp_board[i][j] = '.'
                                            succList.append(copy.deepcopy(temp_board))
                                        else:
                                            break
                                break
                            else:
                                break

                    # backward direction
                    for num in range(1, i + 1):
                        temp_board = copy.deepcopy(board)

                        if valid_index([i - num, j], N, N):

                            if temp_board[i - num][j] in 'wW@':
                                break

                            if temp_board[i - num][j] == '.':
                                temp_board[i - num][j] = '@'
                                temp_board[i][j] = '.'
                                succList.append(copy.deepcopy(temp_board))

                            elif temp_board[i - num][j] in 'bB$':
                                for index in range(1, i + 1):
                                    temp_board = copy.deepcopy(board)
                                    if valid_index([i - num - index, j], N, N):

                                        if temp_board[i - num - index][j] == '.':
                                            temp_board[i - num - index][j] = "@"
                                            temp_board[i - num][j] = '.'
                                            temp_board[i][j] = '.'
                                            succList.append(copy.deepcopy(temp_board))
                                        else:
                                            break
                                break
                            else:
                                break

                    # forward direction
                    for num in range(1, size - i):
                        temp_board = copy.deepcopy(board)

                        if valid_index([i + num, j], N, N):

                            if temp_board[i + num][j] in 'wW@':
                                break

                            if temp_board[i + num][j] == '.':
                                temp_board[i + num][j] = '@'
                                temp_board[i][j] = '.'
                                succList.append(copy.deepcopy(temp_board))

                            elif temp_board[i + num][j] in 'bB$':
                                for index in range(1, size - i):
                                    temp_board = copy.deepcopy(board)
                                    if valid_index([i + num + index, j], N, N):

                                        if temp_board[i + num + index][j] == '.':
                                            temp_board[i + num + index][j] = "@"
                                            temp_board[i + num][j] = '.'
                                            temp_board[i][j] = '.'
                                            succList.append(copy.deepcopy(temp_board))
                                        else:
                                            break

                                break
                            else:
                                break

                    # lower left diagonal direction
                    for num in range(1, size - i - j):
                        temp_board = copy.deepcopy(board)

                        if valid_index([i + num, j - num], N, N):

                            if temp_board[i + num][j - num] in 'wW@':
                                break

                            if temp_board[i + num][j - num] == '.':
                                temp_board[i + num][j - num] = '@'
                                temp_board[i][j] = '.'
                                succList.append(copy.deepcopy(temp_board))

                            elif temp_board[i + num][j - num] in 'bB$':
                                for index in range(1, size - i - j):
                                    temp_board = copy.deepcopy(board)
                                    if valid_index([i + num + index, j - num - index], N, N):

                                        if temp_board[i + num + index][j - num - index] == '.':
                                            temp_board[i + num + index][j - num - index] = "@"
                                            temp_board[i + num][j - num] = '.'
                                            temp_board[i][j] = '.'
                                            succList.append(copy.deepcopy(temp_board))
                                        else:
                                            break
                                break
                            else:
                                break

                    # lower right diagonal direction
                    for num in range(1, size - i - j):
                        temp_board = copy.deepcopy(board)

                        if valid_index([i + num, j + num], N, N):

                            if temp_board[i + num][j + num] in 'wW@':
                                break

                            if temp_board[i + num][j + num] == '.':
                                temp_board[i + num][j + num] = '@'
                                temp_board[i][j] = '.'
                                succList.append(copy.deepcopy(temp_board))

                            elif temp_board[i + num][j + num] in 'bB$':
                                for index in range(1, size - i - j):
                                    temp_board = copy.deepcopy(board)
                                    if valid_index([i + num + index, j + num + index], N, N):

                                        if temp_board[i + num + index][j + num + index] == '.':
                                            temp_board[i + num + index][j + num + index] = "@"
                                            temp_board[i + num][j + num] = '.'
                                            temp_board[i][j] = '.'
                                            succList.append(copy.deepcopy(temp_board))
                                        else:
                                            break
                                break
                            else:
                                break

                    # upper left diagonal direction
                    for num in range(1, size - i + 1):
                        temp_board = copy.deepcopy(board)

                        if valid_index([i - num, j - num], N, N):

                            if temp_board[i - num][j - num] in 'wW@':
                                break

                            if temp_board[i - num][j - num] == '.':
                                temp_board[i - num][j - num] = '@'
                                temp_board[i][j] = '.'
                                succList.append(copy.deepcopy(temp_board))

                            elif temp_board[i - num][j - num] in 'bB$':
                                for index in range(1, size - i + 1):
                                    temp_board = copy.deepcopy(board)
                                    if valid_index([i - num - index, j - num - index], N, N):

                                        if temp_board[i - num - index][j - num - index] == '.':
                                            temp_board[i - num - index][j - num - index] = "@"
                                            temp_board[i - num][j - num] = '.'
                                            temp_board[i][j] = '.'
                                            succList.append(copy.deepcopy(temp_board))
                                        else:
                                            break
                                break
                            else:
                                break

                    # upper right diagonal direction
                    for num in range(1, size - i + 1):
                        temp_board = copy.deepcopy(board)

                        if valid_index([i - num, j + num], N, N):

                            if temp_board[i - num][j + num] in 'wW@':
                                break

                            if temp_board[i - num][j + num] == '.':
                                temp_board[i - num][j + num] = '@'
                                temp_board[i][j] = '.'
                                succList.append(copy.deepcopy(temp_board))

                            elif temp_board[i - num][j + num] in 'bB$':
                                for index in range(1, size - i + 1):
                                    temp_board = copy.deepcopy(board)
                                    if valid_index([i - num - index, j + num + index], N, N):

                                        if temp_board[i - num - index][j + num + index] == '.':
                                            temp_board[i - num - index][j + num + index] = "@"
                                            temp_board[i - num][j + num] = '.'
                                            temp_board[i][j] = '.'
                                            succList.append(copy.deepcopy(temp_board))
                                        else:
                                            break
                                break
                            else:
                                break

    else:
        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if value == "$":

                    # left side
                    for num in range(1, j + 1):
                        temp_board = copy.deepcopy(board)

                        if valid_index([i, j - num], N, N):
                            if temp_board[i][j - num] == '.':
                                temp_board[i][j - num] = '$'
                                temp_board[i][j] = '.'
                                succList.append(copy.deepcopy(temp_board))

                            elif temp_board[i][j - num] in 'wW@':
                                for index in range(1, j + 1):
                                    temp_board = copy.deepcopy(board)
                                    if valid_index([i, j - num - index], N, N):
                                        if temp_board[i][j - num - index] == '.':
                                            temp_board[i][j - num - index] = "$"
                                            temp_board[i][j - num] = '.'
                                            temp_board[i][j] = '.'
                                            succList.append(copy.deepcopy(temp_board))
                                        else:
                                            break
                                break
                            else:
                                break

                    # right side
                    for num in range(1, size - j):
                        temp_board = copy.deepcopy(board)

                        if valid_index([i, j + num], N, N):
                            if temp_board[i][j + num] == '.':
                                temp_board[i][j + num] = '$'
                                temp_board[i][j] = '.'
                                succList.append(copy.deepcopy(temp_board))

                            elif temp_board[i][j + num] in 'wW@':
                                for index in range(1, j + num):
                                    temp_board = copy.deepcopy(board)
                                    if valid_index([i, j + num + index], N, N):
                                        if temp_board[i][j + num + index] == '.':
                                            temp_board[i][j + num + index] = "$"
                                            temp_board[i][j + num] = '.'
                                            temp_board[i][j] = '.'
                                            succList.append(copy.deepcopy(temp_board))
                                        else:
                                            break
                                break
                            else:
                                break

                    # backward direction
                    for num in range(1, i + 1):
                        temp_board = copy.deepcopy(board)

                        if valid_index([i - num, j], N, N):

                            if temp_board[i - num][j] in 'bB$':
                                break

                            if temp_board[i - num][j] == '.':
                                temp_board[i - num][j] = '$'
                                temp_board[i][j] = '.'
                                succList.append(copy.deepcopy(temp_board))

                            elif temp_board[i - num][j] in 'wW@':
                                for index in range(1, i + 1):
                                    temp_board = copy.deepcopy(board)
                                    if valid_index([i - num - index, j], N, N):

                                        if temp_board[i - num - index][j] == '.':
                                            temp_board[i - num - index][j] = "$"
                                            temp_board[i - num][j] = '.'
                                            temp_board[i][j] = '.'
                                            succList.append(copy.deepcopy(temp_board))
                                        else:
                                            break
                                break
                            else:
                                break

                    # forward direction
                    for num in range(1, size - i):
                        temp_board = copy.deepcopy(board)

                        if valid_index([i + num, j], N, N):

                            if temp_board[i + num][j] in 'bB$':
                                break

                            if temp_board[i + num][j] == '.':
                                temp_board[i + num][j] = '$'
                                temp_board[i][j] = '.'
                                succList.append(copy.deepcopy(temp_board))

                            elif temp_board[i + num][j] in 'wW@':
                                for index in range(1, size - i):
                                    temp_board = copy.deepcopy(board)
                                    if valid_index([i + num + index, j], N, N):

                                        if temp_board[i + num + index][j] == '.':
                                            temp_board[i + num + index][j] = "$"
                                            temp_board[i + num][j] = '.'
                                            temp_board[i][j] = '.'
                                            succList.append(copy.deepcopy(temp_board))
                                        else:
                                            break
                                break
                            else:
                                break

                    # lower left diagonal direction
                    for num in range(1, size - i - j):
                        temp_board = copy.deepcopy(board)

                        if valid_index([i + num, j - num], N, N):

                            if temp_board[i + num][j - num] in 'bB$':
                                break

                            if temp_board[i + num][j - num] == '.':
                                temp_board[i + num][j - num] = '$'
                                temp_board[i][j] = '.'
                                succList.append(copy.deepcopy(temp_board))

                            elif temp_board[i + num][j - num] in 'wW@':
                                for index in range(1, size - i - j):
                                    temp_board = copy.deepcopy(board)
                                    if valid_index([i + num + index, j - num - index], N, N):

                                        if temp_board[i + num + index][j - num - index] == '.':
                                            temp_board[i + num + index][j - num - index] = "$"
                                            temp_board[i + num][j - num] = '.'
                                            temp_board[i][j] = '.'
                                            succList.append(copy.deepcopy(temp_board))
                                        else:
                                            break
                                break
                            else:
                                break

                    # lower right diagonal direction
                    for num in range(1, size - i - j):
                        temp_board = copy.deepcopy(board)

                        if valid_index([i + num, j + num], N, N):

                            if temp_board[i + num][j + num] in 'bB$':
                                break

                            if temp_board[i + num][j + num] == '.':
                                temp_board[i + num][j + num] = '$'
                                temp_board[i][j] = '.'
                                succList.append(copy.deepcopy(temp_board))

                            elif temp_board[i + num][j + num] in 'wW@':
                                for index in range(1, size - i - j):
                                    temp_board = copy.deepcopy(board)
                                    if valid_index([i + num + index, j + num + index], N, N):

                                        if temp_board[i + num + index][j + num + index] == '.':
                                            temp_board[i + num + index][j + num + index] = "$"
                                            temp_board[i + num][j + num] = '.'
                                            temp_board[i][j] = '.'
                                            succList.append(copy.deepcopy(temp_board))
                                        else:
                                            break
                                break
                            else:
                                break

                    # upper left diagonal direction
                    for num in range(1, size - i + 1):
                        temp_board = copy.deepcopy(board)

                        if valid_index([i - num, j - num], N, N):


                            if temp_board[i - num][j - num] in 'bB$':
                                break

                            if temp_board[i - num][j - num] == '.':
                                temp_board[i - num][j - num] = '$'
                                temp_board[i][j] = '.'
                                succList.append(copy.deepcopy(temp_board))

                            elif temp_board[i - num][j - num] in 'wW@':
                                for index in range(1, size - i + 1):
                                    temp_board = copy.deepcopy(board)
                                    if valid_index([i - num - index, j - num - index], N, N):

                                        if temp_board[i - num - index][j - num - index] == '.':
                                            temp_board[i - num - index][j - num - index] = "$"
                                            temp_board[i - num][j - num] = '.'
                                            temp_board[i][j] = '.'
                                            succList.append(copy.deepcopy(temp_board))
                                        else:
                                            break
                                break
                            else:
                                break

                    # upper right diagonal direction
                    for num in range(1, size - i + 1):
                        temp_board = copy.deepcopy(board)

                        if valid_index([i - num, j + num], N, N):

                            if temp_board[i - num][j + num] in 'bB$':
                                break

                            if temp_board[i - num][j + num] == '.':
                                temp_board[i - num][j + num] = '$'
                                temp_board[i][j] = '.'
                                succList.append(copy.deepcopy(temp_board))

                            elif temp_board[i - num][j + num] in 'wW@':
                                for index in range(1, size - i + 1):
                                    temp_board = copy.deepcopy(board)
                                    if valid_index([i - num - index, j + num + index], N, N):

                                        if temp_board[i - num - index][j + num + index] == '.':
                                            temp_board[i - num - index][j + num + index] = "$"
                                            temp_board[i - num][j + num] = '.'
                                            temp_board[i][j] = '.'
                                            succList.append(copy.deepcopy(temp_board))
                                        else:
                                            break
                                break
                            else:
                                break
    return succList



# def raichu_moves(board, size, player):
#     # To check left and right movement - "..b@B...W.W.W.W..w.w.w.w................b.b.b.b..B.B.B.B........"
#
#     # player = "@"
#     succList = []
#     if player == "w":
#         for i, row in enumerate(board):
#             for j, value in enumerate(row):
#                 if value == "@":
#
#                     # left side
#                     for num in range(1, j+1):
#                         temp_board = copy.deepcopy(board)
#
#                         if valid_index([i, j - num], N, N):
#                             if temp_board[i][j - num] == '.':
#                                 temp_board[i][j - num] = '@'
#                                 temp_board[i][j] = '.'
#                                 succList.append(copy.deepcopy(temp_board))
#
#                             elif temp_board[i][j - num] in 'bB':
#                                 for index in range(1,j+1):
#                                     temp_board = copy.deepcopy(board)
#                                     if valid_index([i, j - num-index], N, N):
#                                         if temp_board[i][j - num-index] == '.':
#                                             temp_board[i][j - num-index] = "@"
#                                             temp_board[i][j - num] = '.'
#                                             temp_board[i][j] = '.'
#                                             succList.append(copy.deepcopy(temp_board))
#                                 break
#
#                     # right side
#                     for num in range(1, size-j):
#                         temp_board = copy.deepcopy(board)
#
#                         if valid_index([i, j + num], N, N):
#                             if temp_board[i][j + num] == '.':
#                                 temp_board[i][j + num] = '@'
#                                 temp_board[i][j] = '.'
#                                 succList.append(copy.deepcopy(temp_board))
#
#                             elif temp_board[i][j + num] in 'bB':
#                                 for index in range(1, j + num):
#                                     temp_board = copy.deepcopy(board)
#                                     if valid_index([i, j + num + index], N, N):
#                                         if temp_board[i][j + num + index] == '.':
#                                             temp_board[i][j + num + index] = "@"
#                                             temp_board[i][j + num] = '.'
#                                             temp_board[i][j] = '.'
#                                             succList.append(copy.deepcopy(temp_board))
#                                 break
#
#                     #backward direction
#                     for num in range(1, i + 1):
#                         temp_board = copy.deepcopy(board)
#
#                         if valid_index([i - num, j], N, N):
#
#                             if temp_board[i - num][j] in 'wW':
#                                 break
#
#                             if temp_board[i - num][j] == '.':
#                                 temp_board[i - num][j] = '@'
#                                 temp_board[i][j] = '.'
#                                 succList.append(copy.deepcopy(temp_board))
#
#                             elif temp_board[i-num][j] in 'bB':
#                                 for index in range(1, i + 1):
#                                     temp_board = copy.deepcopy(board)
#                                     if valid_index([i - num - index, j], N, N):
#
#                                         if temp_board[i - num - index][j] == '.':
#                                             temp_board[i - num - index][j] = "@"
#                                             temp_board[i-num][j] = '.'
#                                             temp_board[i][j] = '.'
#                                             succList.append(copy.deepcopy(temp_board))
#                                 break
#
#                     # forward direction
#                     for num in range(1, size-i):
#                         temp_board = copy.deepcopy(board)
#
#                         if valid_index([i + num, j], N, N):
#
#                             if temp_board[i + num][j] in 'wW':
#                                 break
#
#                             if temp_board[i + num][j] == '.':
#                                 temp_board[i + num][j] = '@'
#                                 temp_board[i][j] = '.'
#                                 succList.append(copy.deepcopy(temp_board))
#
#                             elif temp_board[i + num][j] in 'bB':
#                                 for index in range(1, size-i):
#                                     temp_board = copy.deepcopy(board)
#                                     if valid_index([i + num + index, j], N, N):
#
#                                         if temp_board[i + num + index][j] == '.':
#                                             temp_board[i + num + index][j] = "@"
#                                             temp_board[i + num][j] = '.'
#                                             temp_board[i][j] = '.'
#                                             succList.append(copy.deepcopy(temp_board))
#                                 break
#
#                     #lower left diagonal direction
#                     for num in range(1, size - i -j):
#                         temp_board = copy.deepcopy(board)
#
#                         if valid_index([i + num, j - num], N, N):
#
#                             if temp_board[i + num][j - num] in 'wW':
#                                 break
#
#                             if temp_board[i + num][j - num] == '.':
#                                 temp_board[i + num][j - num] = '@'
#                                 temp_board[i][j] = '.'
#                                 succList.append(copy.deepcopy(temp_board))
#
#                             elif temp_board[i + num][j - num] in 'bB':
#                                 for index in range(1, size - i -j):
#                                     temp_board = copy.deepcopy(board)
#                                     if valid_index([i + num + index, j - num - index], N, N):
#
#                                         if temp_board[i + num + index][j - num - index] == '.':
#                                             temp_board[i + num + index][j - num - index] = "@"
#                                             temp_board[i + num][j - num] = '.'
#                                             temp_board[i][j] = '.'
#                                             succList.append(copy.deepcopy(temp_board))
#                                         else:
#                                             break
#                                 break
#
#                     # lower right diagonal direction
#                     for num in range(1, size - i-j):
#                         temp_board = copy.deepcopy(board)
#
#                         if valid_index([i + num, j + num], N, N):
#
#                             if temp_board[i + num][j + num] in 'wW':
#                                 break
#
#                             if temp_board[i + num][j + num] == '.':
#                                 temp_board[i + num][j + num] = '@'
#                                 temp_board[i][j] = '.'
#                                 succList.append(copy.deepcopy(temp_board))
#
#                             elif temp_board[i + num][j + num] in 'bB':
#                                 for index in range(1, size - i-j):
#                                     temp_board = copy.deepcopy(board)
#                                     if valid_index([i + num + index, j + num + index], N, N):
#
#                                         if temp_board[i + num + index][j + num + index] == '.':
#                                             temp_board[i + num + index][j + num + index] = "@"
#                                             temp_board[i + num][j + num] = '.'
#                                             temp_board[i][j] = '.'
#                                             succList.append(copy.deepcopy(temp_board))
#                                         else:
#                                             break
#                                 break
#
#                     # upper left diagonal direction
#                     for num in range(1, size - i +1):
#                         temp_board = copy.deepcopy(board)
#
#                         if valid_index([i - num, j - num], N, N):
#
#                             if temp_board[i - num][j - num] in 'wW':
#                                 break
#
#                             if temp_board[i - num][j - num] == '.':
#                                 temp_board[i - num][j - num] = '@'
#                                 temp_board[i][j] = '.'
#                                 succList.append(copy.deepcopy(temp_board))
#
#                             elif temp_board[i - num][j - num] in 'bB':
#                                 for index in range(1, size - i+1):
#                                     temp_board = copy.deepcopy(board)
#                                     if valid_index([i - num - index, j - num - index], N, N):
#
#                                         if temp_board[i - num - index][j - num - index] == '.':
#                                             temp_board[i - num - index][j - num - index] = "@"
#                                             temp_board[i - num][j - num] = '.'
#                                             temp_board[i][j] = '.'
#                                             succList.append(copy.deepcopy(temp_board))
#                                         else:
#                                             break
#                                 break
#
#                     # upper right diagonal direction
#                     for num in range(1, size - i + 1):
#                         temp_board = copy.deepcopy(board)
#
#                         if valid_index([i + num, j - num], N, N):
#
#                             if temp_board[i + num][j - num] in 'wW':
#                                 break
#
#                             if temp_board[i + num][j - num] == '.':
#                                 temp_board[i + num][j - num] = '@'
#                                 temp_board[i][j] = '.'
#                                 succList.append(copy.deepcopy(temp_board))
#
#                             elif temp_board[i + num][j - num] in 'bB':
#                                 for index in range(1, size - i + 1):
#                                     temp_board = copy.deepcopy(board)
#                                     if valid_index([i + num + index, j - num - index], N, N):
#
#                                         if temp_board[i + num + index][j - num - index] == '.':
#                                             temp_board[i + num + index][j - num - index] = "@"
#                                             temp_board[i + num][j - num] = '.'
#                                             temp_board[i][j] = '.'
#                                             succList.append(copy.deepcopy(temp_board))
#                                         else:
#                                             break
#                                 break
#
#     else:
#         for i, row in enumerate(board):
#             for j, value in enumerate(row):
#                 if value == "$":
#
#                     # left side
#                     for num in range(1, j+1):
#                         temp_board = copy.deepcopy(board)
#
#                         if valid_index([i, j - num], N, N):
#                             if temp_board[i][j - num] == '.':
#                                 temp_board[i][j - num] = '$'
#                                 temp_board[i][j] = '.'
#                                 succList.append(copy.deepcopy(temp_board))
#
#                             elif temp_board[i][j - num] in 'wW':
#                                 for index in range(1,j+1):
#                                     temp_board = copy.deepcopy(board)
#                                     if valid_index([i, j - num-index], N, N):
#                                         if temp_board[i][j - num-index] == '.':
#                                             temp_board[i][j - num-index] = "$"
#                                             temp_board[i][j - num] = '.'
#                                             temp_board[i][j] = '.'
#                                             succList.append(copy.deepcopy(temp_board))
#                                 break
#
#                     # right side
#                     for num in range(1, size-j):
#                         temp_board = copy.deepcopy(board)
#
#                         if valid_index([i, j + num], N, N):
#                             if temp_board[i][j + num] == '.':
#                                 temp_board[i][j + num] = '$'
#                                 temp_board[i][j] = '.'
#                                 succList.append(copy.deepcopy(temp_board))
#
#                             elif temp_board[i][j + num] in 'wW':
#                                 for index in range(1, j + num):
#                                     temp_board = copy.deepcopy(board)
#                                     if valid_index([i, j + num + index], N, N):
#                                         if temp_board[i][j + num + index] == '.':
#                                             temp_board[i][j + num + index] = "$"
#                                             temp_board[i][j + num] = '.'
#                                             temp_board[i][j] = '.'
#                                             succList.append(copy.deepcopy(temp_board))
#                                 break
#
#                     #backward direction
#                     for num in range(1, i + 1):
#                         temp_board = copy.deepcopy(board)
#
#                         if valid_index([i - num, j], N, N):
#
#                             if temp_board[i - num][j] in 'bB':
#                                 break
#
#                             if temp_board[i - num][j] == '.':
#                                 temp_board[i - num][j] = '$'
#                                 temp_board[i][j] = '.'
#                                 succList.append(copy.deepcopy(temp_board))
#
#                             elif temp_board[i-num][j] in 'wW':
#                                 for index in range(1, i + 1):
#                                     temp_board = copy.deepcopy(board)
#                                     if valid_index([i - num - index, j], N, N):
#
#                                         if temp_board[i - num - index][j] == '.':
#                                             temp_board[i - num - index][j] = "$"
#                                             temp_board[i-num][j] = '.'
#                                             temp_board[i][j] = '.'
#                                             succList.append(copy.deepcopy(temp_board))
#                                 break
#
#                     # forward direction
#                     for num in range(1, size-i):
#                         temp_board = copy.deepcopy(board)
#
#                         if valid_index([i + num, j], N, N):
#
#                             if temp_board[i + num][j] in 'bB':
#                                 break
#
#                             if temp_board[i + num][j] == '.':
#                                 temp_board[i + num][j] = '$'
#                                 temp_board[i][j] = '.'
#                                 succList.append(copy.deepcopy(temp_board))
#
#                             elif temp_board[i + num][j] in 'wW':
#                                 for index in range(1, size-i):
#                                     temp_board = copy.deepcopy(board)
#                                     if valid_index([i + num + index, j], N, N):
#
#                                         if temp_board[i + num + index][j] == '.':
#                                             temp_board[i + num + index][j] = "$"
#                                             temp_board[i + num][j] = '.'
#                                             temp_board[i][j] = '.'
#                                             succList.append(copy.deepcopy(temp_board))
#                                 break
#
#                     #lower left diagonal direction
#                     for num in range(1, size - i -j):
#                         temp_board = copy.deepcopy(board)
#
#                         if valid_index([i + num, j - num], N, N):
#
#                             if temp_board[i + num][j - num] in 'bB':
#                                 break
#
#                             if temp_board[i + num][j - num] == '.':
#                                 temp_board[i + num][j - num] = '$'
#                                 temp_board[i][j] = '.'
#                                 succList.append(copy.deepcopy(temp_board))
#
#                             elif temp_board[i + num][j - num] in 'wW':
#                                 for index in range(1, size - i -j):
#                                     temp_board = copy.deepcopy(board)
#                                     if valid_index([i + num + index, j - num - index], N, N):
#
#                                         if temp_board[i + num + index][j - num - index] == '.':
#                                             temp_board[i + num + index][j - num - index] = "$"
#                                             temp_board[i + num][j - num] = '.'
#                                             temp_board[i][j] = '.'
#                                             succList.append(copy.deepcopy(temp_board))
#                                         else:
#                                             break
#                                 break
#
#                     # lower right diagonal direction
#                     for num in range(1, size - i-j):
#                         temp_board = copy.deepcopy(board)
#
#                         if valid_index([i + num, j + num], N, N):
#
#                             if temp_board[i + num][j + num] in 'bB':
#                                 break
#
#                             if temp_board[i + num][j + num] == '.':
#                                 temp_board[i + num][j + num] = '$'
#                                 temp_board[i][j] = '.'
#                                 succList.append(copy.deepcopy(temp_board))
#
#                             elif temp_board[i + num][j + num] in 'wW':
#                                 for index in range(1, size - i-j):
#                                     temp_board = copy.deepcopy(board)
#                                     if valid_index([i + num + index, j + num + index], N, N):
#
#                                         if temp_board[i + num + index][j + num + index] == '.':
#                                             temp_board[i + num + index][j + num + index] = "$"
#                                             temp_board[i + num][j + num] = '.'
#                                             temp_board[i][j] = '.'
#                                             succList.append(copy.deepcopy(temp_board))
#                                         else:
#                                             break
#                                 break
#
#                     # upper left diagonal direction
#                     for num in range(1, size - i +1):
#                         temp_board = copy.deepcopy(board)
#
#                         if valid_index([i - num, j - num], N, N):
#
#                             if temp_board[i - num][j - num] in 'bB':
#                                 break
#
#                             if temp_board[i - num][j - num] == '.':
#                                 temp_board[i - num][j - num] = '$'
#                                 temp_board[i][j] = '.'
#                                 succList.append(copy.deepcopy(temp_board))
#
#                             elif temp_board[i - num][j - num] in 'wW':
#                                 for index in range(1, size - i+1):
#                                     temp_board = copy.deepcopy(board)
#                                     if valid_index([i - num - index, j - num - index], N, N):
#
#                                         if temp_board[i - num - index][j - num - index] == '.':
#                                             temp_board[i - num - index][j - num - index] = "$"
#                                             temp_board[i - num][j - num] = '.'
#                                             temp_board[i][j] = '.'
#                                             succList.append(copy.deepcopy(temp_board))
#                                         else:
#                                             break
#                                 break
#
#                     # upper right diagonal direction
#                     for num in range(1, size - i + 1):
#                         temp_board = copy.deepcopy(board)
#
#                         if valid_index([i + num, j - num], N, N):
#
#                             if temp_board[i + num][j - num] in 'bB':
#                                 break
#
#                             if temp_board[i + num][j - num] == '.':
#                                 temp_board[i + num][j - num] = '$'
#                                 temp_board[i][j] = '.'
#                                 succList.append(copy.deepcopy(temp_board))
#
#                             elif temp_board[i + num][j - num] in 'wW':
#                                 for index in range(1, size - i + 1):
#                                     temp_board = copy.deepcopy(board)
#                                     if valid_index([i + num + index, j - num - index], N, N):
#
#                                         if temp_board[i + num + index][j - num - index] == '.':
#                                             temp_board[i + num + index][j - num - index] = "$"
#                                             temp_board[i + num][j - num] = '.'
#                                             temp_board[i][j] = '.'
#                                             succList.append(copy.deepcopy(temp_board))
#                                         else:
#                                             break
#                                 break
#
#
#     return succList
'''
def successor(board,player):
    succ=[]
    for y in board:
        for x in y:
            if x=='w':
                succ.append(pichu_moves(b, N, player))
            if x=='W':
                succ.append(pikachu_move(b, N, player))
            if x=='@':
                succ.append(raichu_moves(b, N, player))
            if x=='b':
                succ.append(pichu_moves(b, N, player))
            if x=='B':
                succ.append(pikachu_moves(b, N, player))
            if x=='$':
                succ.append(raichu_moves(b, N, player))
    return succ
'''

def succ1(board,player_color,N):
    succ=[];b = [];N=8
    k = 0;ans=[]
    #make board into list of lists
    b=board.copy()
    if player_color.lower()=='w':
        succ.append(pichu_moves(b, N, 'w'))
        succ.append(pikachu_moves(b, N, "W"))
        succ.append(raichu_moves(b, N, '@'))
    else:
        succ.append(pichu_moves(b, N, 'b'))
        succ.append(pikachu_moves(b, N, 'B'))
        succ.append(raichu_moves(b, N, '$'))
    for i in succ:
        for j in i:
            ans.append(j)

    return ans

def alphabeta(board,alpha,beta,player,N):
    
    
    initial_max=-9999999999999;
    result=[];
    succ_list = succ1(board, player, N)
    for succ in succ_list:
        temp=minfunction(succ,alpha,beta,2,player,N)
        if temp>initial_max:
            initial_max=temp
            result=succ
    return result
    
        
              
def minfunction(board,alpha,beta,depth,player,N):
    depth+=1
    localmin=999999999999
    if player=='w':
        minplayer='b'
    else:
        minplayer='w'

    if depth<4:
        for succ in succ1(board,minplayer,N):
            value=maxfunction(succ,alpha,beta,depth,minplayer,N)
            if value<localmin:
                localmin=value
            if value<=alpha:
                return localmin
            if value<beta:
                beta=value
    if depth>=4:
        for succ in succ1(board,minplayer,N):
            value=evaluation_function(succ,minplayer)
            if value<localmin:
                localmin=value

           
    return localmin

def maxfunction(board,alpha,beta,depth,player,N):
    depth+=1
    localmax=-999999999999
    if player=='b':
        maxplayer='w'
    else:
        maxplayer='b'
    if depth<4:
        for succ in succ1(board,maxplayer,N):
            value=minfunction(succ,alpha,beta,depth,maxplayer,N)
            if value>localmax:
                localmax=value
            if value>=beta:
                return localmax
            if value>alpha:
                alpha=value


    if depth>=4:
        for succ in succ1(board,maxplayer,N):
            value=evaluation_function(succ,maxplayer)
            if value>localmax:
                localmax=value
       
                
    return localmax

def evaluation_function(board,player):
    count_wpichu,count_Wpikachu, count_bpichu, count_Bpikachu, count_wraichu, count_braichu = 0, 0, 0, 0, 0, 0
    count=0
    rowNum=0
    for j in board:
        count+=1
        for i in j:
            if i=='w':
                rowNum+=count
                count_wpichu+=1
            if i=='b':
                count_bpichu+=1
            if i=='W':
                count_Wpikachu+=1
            if i=='B':
                count_Bpikachu+=1
            if i=='@':
                count_wraichu+=1
            if i=='$':
                count_braichu+=1
                
            
    kill_pichu=count_wpichu-count_bpichu
    kill_raichu=count_wraichu-count_braichu
    kill_pikachu=count_Wpikachu-count_Bpikachu


    if player=='w':
        best_move = len(board) * 6 * kill_pichu + len(board) * 8 * kill_pikachu + 3 * rowNum + len(board) * 8 * kill_raichu + len(board)* 7 * count_wraichu
        return best_move
    else:
        best_move = len(board) * 6 * kill_pichu + len(board) * 8 * kill_pikachu + 3 * rowNum + len(board) * 8 * kill_raichu + len(board)* 7 * count_braichu
        return best_move*-1

def is_Terminal(board_array,player):
    white=0;black=0
    for row in board_array:
        for col in board_array:
            if col=='w' or col=='W':
                white=+1
            if col=='b' or col=='B':
                black=+1
   
    if player=='w':
        if white==white-black:
            return 1
        elif -black==white-black:
            return -1
   
    if player=='b':
        if white==white-black:
            return -1
        elif -black==white-black:
            return 1

if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise Exception("Usage: Raichu.py N player board timelimit")
        
    (_, N, player, board, timelimit) = sys.argv
    N=int(N)
    timelimit=int(timelimit)
    if player not in "wb":
        raise Exception("Invalid player.")

    if len(board) != N*N or 0 in [c in "wb.WB@$" for c in board]:
        raise Exception("Bad board string.")

    print("Searching for best move for " + player + " from board state: \n" + board_to_string(board, N))
    print("Here's what I decided:")
    kkk=find_best_move(board, N, player, timelimit)
    print(kkk)
