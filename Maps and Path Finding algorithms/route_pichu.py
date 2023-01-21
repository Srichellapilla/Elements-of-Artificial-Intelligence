#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : [Sri Varsha Chellapilla USERNAME: srchell UID: 2000930415]
#
# Based on skeleton code provided in CSCI B551, Fall 2021.

import sys

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
            return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]
                
# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
        moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))
        #print(moves)

        # Return only moves that are within the house_map and legal (i.e. go through open space ".")
        d=[ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]
        o=[]
        for m in d:
            l=''
            if row-m[0]==1:
                l= 'U'
            if row-m[0]==-1:
                l= 'D'
            if col-m[1]==1:
                l= 'L'
            if col-m[1]==-1:
                l= 'R'
            o.append((m,l))
        return o



def search(house_map):
        # Find pichu start position
        pichu_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"][0]
        fringe=[(pichu_loc,0,'')]
        visited=[]
        #print(fringe)

        while fringe:
                #print(fringe)
                (curr_move, curr_dist,direction)=fringe.pop(0)
                #print(curr_move, curr_dist,direction)
                for move in moves(house_map, *curr_move):
                        #print(move)
                        if house_map[move[0][0]][move[0][1]]=="@":
                                return (curr_dist+1, True,direction) 
                        else:
                                #print('ccc',move)
                                if move[0] not in visited:
                                    fringe.append((move[0], curr_dist + 1,direction+move[1]))
                                    visited.append(move[0])
        return (0,False,'')

# Main Function
if __name__ == "__main__":
        house_map=parse_map(sys.argv[1])
        print("Shhhh... quiet while I navigate!")
        #print(house_map)
        solution = search(house_map)
        print("Here's the solution I found:")
        print(str(solution[0]) , solution[1],solution[2])
