#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : [Sri Varsha Chellapilla USERNAME: srchell UID:2000930415]
#
# Based on skeleton code in CSCI B551, Fall 2021.

import sys

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]

# Count total # of pichus on house_map


def count_pichus(house_map):
    return sum([ row.count('p') for row in house_map ] )

# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    return "\n".join(["".join(row) for row in house_map])

# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    return house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]

#checking if pichu can be placed on the upper rows based on current pichu position
def checkup(house_map,r,c):
    for row in range(r,-1,-1):
        if house_map[row][c]=='p':
            return False
    return True


#checking if pichu can be placed on the left of the current pichu position 
def checkleft(house_map,r,c):
    for col in range(c,-1,-1):
        if house_map[r][col]=='p':
            return False
    return True

#checking if pichu can be placed on the right of the current pichu position
def checkright(house_map,r,c):
    for col in range(c,len(house_map[0]),1):
        if house_map[r][col]=='p':
            return False
    return True

#checking if pichu can be placed below the current pichu position
def checkdown(house_map,r,c):
    for row in range(r,len(house_map),1):
        if house_map[row][c]=='p':
            return False
    return True

#checking if pichu has diagonal conflict
#checking if pichu has lower left diagonal conflict
def leftlowerdiag(house_map,r,c):
    while(r<len(house_map)-1 and c >= 0):
        r=r+1
        c=c-1
        if c < 0 or r > len(house_map)-1:
            break
        if(house_map[r][c]=='p'):
            return False
        if(house_map[r][c] in ['X','@']):
            break
    return True

#checking if pichu has upper left conflict
def leftupperdiag(house_map,r,c):
    while(r >= 0 and c >= 0 ):
        r=r-1
        c=c-1
        if c<0  or r>len(house_map[0])-1:
            break
        if(house_map[r][c] == 'p'):
            return False
        if(house_map[r][c] in ['x','@']):
            break
    return True
    


#checking if pichu has lower right diagonal conflict
def rightlowerdiag(house_map,r,c):
    while (r<len(house_map)-1 and c<len(house_map[0])-1):
        r =r+1
        c =c+1
        if r>(len(house_map))-1 or c>len(house_map[0])-1:
            break
        if(house_map[r][c]=='p'):
            return False
        if(house_map[r][c] in ['X','@']):
            break
    return True

#checking if pichu has upper right diagonal conflict
def rightupperdiag(house_map,r,c):
    while(r >= 0 and c <len(house_map[0])-1):
        r=r-1
        c=c+1
        if r<0 or c>len(house_map[0])-1:
            break
        if(house_map[r][c] == 'p'):
            return False
        if(house_map[r][c] in ['X','@']):
            break
    return True
        
#check valid move
def validmove(house_map,r,c):
    if checkup(house_map,r,c) and checkdown(house_map,r,c) and checkleft(house_map,r,c) and checkright(house_map,r,c) and leftlowerdiag(house_map,r,c) and rightlowerdiag(house_map,r,c) and rightupperdiag(house_map,r,c) and leftupperdiag(house_map,r,c):
        return True
    return False

# Get list of successors of given house_map state
def successors(house_map):
    return [ add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) if house_map[r][c] == '.' and validmove(house_map,r,c)]

# check if house_map is a goal state
def is_goal(house_map, k):
    return count_pichus(house_map) == k 

# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_house_map, success), where:
# - new_house_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_house_map,k):
    
    fringe = [initial_house_map]
    while len(fringe) > 0:
        for new_house_map in successors( fringe.pop(0) ):
            if is_goal(new_house_map,k):
                return(new_house_map,True)
            fringe.append(new_house_map)

if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map,k)
    print ("Here's what we found:")
    print (printable_house_map(solution[0]) if solution[1] else "False")
           
