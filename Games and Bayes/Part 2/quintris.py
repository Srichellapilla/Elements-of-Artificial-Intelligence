# Simple quintris program! v0.2
# D. Crandall, Sept 2021

from AnimatedQuintris import *
from SimpleQuintris import *
from kbinput import *
import time, sys
from numpy import random
import numpy as np
from QuintrisGame import *
import copy
import heapq

class HumanPlayer:
    def get_moves(self, quintris):
        print("Type a sequence of moves using: \n  b for move left \n  m for move right \n  n for rotation\n  h for horizontal flip\nThen press enter. E.g.: bbbnn\n")
        moves = input()
        return moves

    def control_game(self, quintris):
        while 1:
            c = get_char_keyboard()
            commands = {"b": quintris.left, "h": quintris.hflip, "n": quintris.rotate, "m": quintris.right, " ": quintris.down}
            commands[c]()

#####
# This is the part you'll want to modify!
# Replace our super simple algorithm with something better
#
class ComputerPlayer:
    #Code from QuintrisGame.py
    def calculateColHeight(self, board, col):
        for row in range(len(board)):
            if board[row][col] == 'x':
                return row
        return len(board)

    def cal_bumpiness(self, board):
        col_heights = []
        for col in range(len(board[0])):
            col_heights.append(len(board) - self.calculateColHeight(board, col))
        bumpiness = 0
        for i in range(len(col_heights)-1):
            bumpiness += abs(col_heights[i] - col_heights[i+1])
        return bumpiness

    def cal_aggregateHeight(self, board):
        agg_height = 0
        for col in range(len(board[0])):
            agg_height += len(board) - self.calculateColHeight(board, col)
        return agg_height

    def cal_holes(self, board):
        holes = 0
        for col in range(len(board[0])):
            columnHeight = self.calculateColHeight(board, col)
            if columnHeight != len(board):
                for i in range(len(board) - 1, columnHeight, -1):
                    if board[i][col] == " ":
                        holes += 1
        return holes

    def cal_completeRows(self, board):
        complete = [i for (i, s) in enumerate(board) if s.count(' ') == 0]
        return len(complete)


    def calculate_cost(self, board):
        # calculate four parameters for board : bumpiness, aggregate height, number of holes, complete rows
        # x1 = -0.510066
        # x2 = -0.35663
        # x3 = 0.760666
        # x4 = -0.184483

        x1 = -5.5
        x2 = -4.5
        x3 = 4
        x4 = -1.8

        col_heights = []
        for col in range(len(board[0])):
            col_heights.append(len(board) - self.calculateColHeight(board, col))

        avg_height = np.mean(col_heights)
        cost = x1 * self.cal_aggregateHeight(board) + x2 * self.cal_holes(board) \
               + x3 * self.cal_completeRows(board) + x4 * self.cal_bumpiness(board)


        # avg_height = np.mean(col_heights)
        # std_height = np.std(col_heights)
        # height_diff = max(col_heights) - min(col_heights)
        # ediff1 = max(abs(np.ediff1d(col_heights)))
        # x1 = -1
        # x2 = -0.15
        # x3 = -0.25
        # x4 = -0.8
        # x5 = -0.65
        # x6 = 0.76
        # cost = x1 * self.cal_holes(board) + x2 * avg_height \
        #        + x3 * std_height + x4 * height_diff \
        #         + x5 * ediff1

        return cost


    def get_successors(self, quintris, all_piece_combinations, next_piece_combinations):
        successors = []
        moves = []

        for piece, move in all_piece_combinations:
            height = len(piece)
            width = len(piece[0])
            board = quintris.get_board()
            for col in range(0, len(board[0])):
                board = quintris.get_board()
                new_move = copy.deepcopy(move)
                # for row in range(len(board)-1, 0, -1):
                #     if board[row][col] == 'x':
                #         continue
                #     else:
                #         row_val = row+1
                #         break
                # col_heights = []
                # for c in range(col, col+width-1):
                #     if c < len(board[0]):
                #         col_heights.append(self.calculateColHeight(board, c))
                # max_height = max(col_heights)
                # flag = False
                for row in range(len(board)):
                    while not QuintrisGame.check_collision(board, 0, piece, row, col):
                        row += 1
                    row -= 1
                    if not QuintrisGame.check_collision(board, 0, piece, row, col):
                        new_board = QuintrisGame.place_piece(board, 0, piece, row, col)
                        #if new_board[0] not in successors:
                            # if flag:
                            #     successors.pop()
                            #     moves.pop()
                        c_val = abs(col - quintris.col)
                        if col > quintris.col:
                            new_move += 'm' * c_val
                        else:
                            new_move += 'b' * c_val
                        successors.append(new_board[0])
                        # flag = True
                        moves.append(new_move)
                        break

        #print("Length: ", len(successors))
        #print("Length of moves : ", len(moves))
        #print(moves)
        succ = list(zip(successors, moves))
        succ1, moves1, fringe = [], [], []
        for board, move in succ:
            for next_piece in next_piece_combinations:
                height = len(next_piece)
                width = len(next_piece[0])
                n_board = copy.deepcopy(board)
                for col in range(0, len(board[0])):
                    new_move = copy.deepcopy(move)
                    # col_heights = []
                    # for c in range(col, col + width - 1):
                    #     if c < len(board[0]):
                    #         col_heights.append(self.calculateColHeight(board, c))
                    # max_height = max(col_heights)
                    # flag = False
                    #for row in range(len(board) - height + 1, 0, -1):
                    for row in range(len(board)):
                        while not QuintrisGame.check_collision(board, 0, next_piece, row, col):
                            row += 1
                        row -= 1
                        if not QuintrisGame.check_collision(n_board, 0, next_piece, row, col):
                            new_board = QuintrisGame.place_piece(n_board, 0, next_piece, row, col)
                            #if new_board[0] not in succ1:
                                # if flag:
                                #     successors.pop()
                                #     moves.pop()
                            succ1.append(new_board[0])
                            #flag = True
                            _val = (self.calculate_cost(new_board[0]), new_board[0], new_move)
                            fringe.append(_val)
                            moves1.append(new_move)
                            break

        #print("Length after 2nd piece: ", len(succ1))
        #print(succ1[-200:])
        #print("Length of moves : ", len(moves1))
        heapq.heapify(fringe)
        return heapq.nlargest(5, fringe)
        #succ2 = list(zip(succ1, moves1))
        #print(succ2[:200])









    # This function should generate a series of commands to move the piece into the "optimal"
    # position. The commands are a string of letters, where b and m represent left and right, respectively,
    # and n rotates. quintris is an object that lets you inspect the board, e.g.:
    #   - quintris.col, quintris.row have the current column and row of the upper-left corner of the 
    #     falling piece
    #   - quintris.get_piece() is the current piece, quintris.get_next_piece() is the next piece after that
    #   - quintris.left(), quintris.right(), quintris.down(), and quintris.rotate() can be called to actually
    #     issue game commands
    #   - quintris.get_board() returns the current state of the board, as a list of strings.
    #
    def get_moves(self, quintris):
        # super simple current algorithm: just randomly move left, right, and rotate a few times
        piece = quintris.get_piece()
        #print("Piece is : ", piece)


        board = quintris.get_board()
        all_piece_combinations = []

        #code to calculate combinations
        rotates = QuintrisGame.rotate_piece(piece[0], 90)
        #print("rotates are: ", rotates)
        moves = []
        for k, i in enumerate([0, 90, 180, 270]):
            r = QuintrisGame.rotate_piece(piece[0], i)
            move = ''
            if r not in all_piece_combinations:
                move += 'n' * k
                all_piece_combinations.append(r)
                moves.append(move)
            r_flip = QuintrisGame.hflip_piece(r)
            if r_flip not in all_piece_combinations:
                move += 'h'
                all_piece_combinations.append(r_flip)
                moves.append(move)
        #print(all_piece_combinations)

        all_combs = list(zip(all_piece_combinations, moves))
        #print(all_combs)

        #calculate next piece rotations:
        next_piece = quintris.get_next_piece()
        #print("Next piece is: ", next_piece)
        next_piece_combinations = []
        for k, i in enumerate([0, 90, 180, 270]):
            r = QuintrisGame.rotate_piece(next_piece, i)
            if r not in next_piece_combinations:
                next_piece_combinations.append(r)
            r_flip = QuintrisGame.hflip_piece(r)
            if r_flip not in next_piece_combinations:
                next_piece_combinations.append(r_flip)

        successors = self.get_successors(quintris, all_combs, next_piece_combinations)
        #print(successors[0])


        return successors[0][2]
       
    # This is the version that's used by the animted version. This is really similar to get_moves,
    # except that it runs as a separate thread and you should access various methods and data in
    # the "quintris" object to control the movement. In particular:
    #   - quintris.col, quintris.row have the current column and row of the upper-left corner of the 
    #     falling piece
    #   - quintris.get_piece() is the current piece, quintris.get_next_piece() is the next piece after that
    #   - quintris.left(), quintris.right(), quintris.down(), and quintris.rotate() can be called to actually
    #     issue game commands
    #   - quintris.get_board() returns the current state of the board, as a list of strings.
    #
    def control_game(self, quintris):
        # another super simple algorithm: just move piece to the least-full column
        while 1:
            time.sleep(0.1)

            board = quintris.get_board()
            column_heights = [min([r for r in range(len(board)-1, 0, -1) if board[r][c] == "x"] + [100,]) for c in range(0, len(board[0]))]
            index = column_heights.index(max(column_heights))

            if(index < quintris.col):
                quintris.left()
            elif(index > quintris.col):
                quintris.right()
            else:
                quintris.down()
            break


###################
#### main program
if __name__ == '__main__':
    (player_opt, interface_opt) = sys.argv[1:3]

    try:
        if player_opt == "human":
            player = HumanPlayer()
        elif player_opt == "computer":
            player = ComputerPlayer()
        else:
            print("unknown player!")

        if interface_opt == "simple":
            quintris = SimpleQuintris()
        elif interface_opt == "animated":
            quintris = AnimatedQuintris()
        else:
            print("unknown interface!")

        quintris.start_game(player)

    except EndOfGame as s:
        print("\n\n\n", s)
