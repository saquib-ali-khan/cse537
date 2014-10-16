# SUDOKU SOLVER

import sys, random
from time import time
from sudokuUtil import *

# Please implement function solve_puzzle
# input puzzle: 2D list, for example:
# [ [0,9,5,0,3,2,0,6,4]
#   [0,0,0,0,6,0,1,0,0]
#   [6,0,0,0,0,0,0,0,0]
#   [2,0,0,9,0,3,0,0,6]
#   [0,7,6,0,0,0,0,0,3]
#   [3,0,0,0,0,0,0,0,0]
#   [9,0,0,5,0,4,7,0,1]
#   [0,5,0,0,2,1,0,9,0]
#   [0,0,8,0,0,6,3,0,5] ]
# Return a 2D list with all 0s replaced by 1 to 9.
# You can utilize argv to distinguish between algorithms
# (basic backtracking or with MRV and forward checking).
# For example: python sudokuSolver.py backtracking

# List of numbers to be inserted in a cell
value = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Transposed puzzle to reduce complexity
def transposePuzzle(puzzle):
    return [[row[i] for row in puzzle] for i in range(9)]

# Grid translator to list
def obtainGrid(puzzle):
    gridS = []
    h = [0, 3]
    while h[1] <= 9:
        w = [0, 3]
        while w[1] <= 9:
            #print h, w
            #[[gridS[row][col] for row in range(h,w)] for col in range(h,w)]
            #grid = [[gridS[row][col] for col in range(w[0], w[1])] for row in range(h[0], h[1])]
            # Flattening the list in right format
            #grid = [item for subgrid in grid for item in subgrid]
            grid = [puzzle[row][col] for col in range(w[0], w[1]) for row in range(h[0], h[1])]
            gridS.append(grid)
            w = [el + 3 for el in w]
        h = [el + 3 for el in h]
    return gridS

# Recursive function to backtrack
def backTrack(puzzle):
    #print "---------"
    # Break cond. for recursion
    r = c = 0
    brk = False
    for rIn, row in enumerate(puzzle):
        for cIn, cell in enumerate(row):
            #print rIn, cIn
            #print puzzle[rIn][cIn]
            if cell == 0:
                r = rIn
                c = cIn
                brk = True
                break
        if brk:
            break
    if not brk:
        #print "Done"
        return [puzzle, True]
    # If any unused cell
    #print r, c, puzzle[r][c]
    valueInst = list(value)
    col = transposePuzzle(puzzle)[c]
    #grid are numbered as 1, 2, 3... along row.
    numGrid = (3 * (r/3)) + (c/3)
    grid = obtainGrid(puzzle)[numGrid]

    # Pick a random value
    #print valueInst
    #val = random.choice(valueInst)
    for val in range(1, 10):
        # If value exists in row, column or grid; RE-pick
        '''
        while val in row or val in col or val in grid:
            if val in valueInst:
                valueInst.remove(val)
            if valueInst:
                #print valueInst
                val = random.choice(valueInst)
            else:
                # unable to pick any suitable value
                #print "WWWWW"
                return [puzzle, False]
        '''
        if (not (val in row)) and (not (val in col)) and (not (val in grid)):
            # Place in puzzle and check if sudoku is solved!
            puzzle[r][c] = val
            #print puzzle
            if backTrack(puzzle)[1]:
                print "........"
                return [puzzle, True]
            # If fail, re-assign to 0
            puzzle[r][c] = 0
    pass # debug brkpt
    #print puzzle
    return [puzzle, False]

def solve_puzzle(puzzle, argv):
    """Solve the sudoku puzzle."""
    # Copy of original puzzle
    quzzle = puzzle

    '''
    print puzzle
    print transPuzzle
    print gridS
    '''
    if True:#argv == "backtracking":
        print backTrack(puzzle)[0]

    return backTrack(puzzle)[0]#load_sudoku('given_solution.txt')

#===================================================#
puzzle = load_sudoku('puzzle.txt')

print "solving ..."
t0 = time()
solution = solve_puzzle(puzzle, sys.argv)
t1 = time()
print "completed. time usage: %f" %(t1 - t0), "secs."

save_sudoku('solution.txt', solution)

