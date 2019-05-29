# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens’ placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

# For example,
# There exist two distinct solutions to the 4-queens puzzle:

# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]

##########################################################################################################################################

import copy

def blocked(grid, pos):
    diff = abs(pos[0] - pos[1])
    s = sum(pos)
    for ii in range(pos[0], len(grid)):
        for jj in range(len(grid[ii])):
            block = False
            if (ii, jj) == pos:
                continue
            if ii == pos[0]:
                block = True
            elif jj == pos[1]:
                block = True
            elif pos[0] >= pos[1] and ii - jj == diff:
                block = True
            elif pos[1] >= pos[0] and jj - ii == diff:
                block = True
            elif ii + jj == s:
                block = True

            if block:
                if grid[ii][jj] == 'Q':
                    return False
                else:
                    grid[ii][jj] = '.'
    return grid

def can_add(A, res, grid, ii, jj, num):
    grid[ii][jj] = 'Q'
    t_grid = blocked(grid, (ii, jj))
    if t_grid == False:
        grid[ii][jj] = 'B'
        return res, False
    elif num == 0:
        return res, grid
    else:
        res, grid = add_queen(A, res, grid, num, ii + 1)
    return res, grid

def add_queen(A, res, grid, num, idx):
    last_grid = copy.deepcopy(grid)
    for ii in range(idx, A):
        last_num = num
        for jj in range(A):
            if grid[ii][jj] == 'B':
                res, t_grid = can_add(A, res, grid, ii, jj, num)
                if t_grid == False:
                    grid = copy.deepcopy(last_grid)
                elif t_grid == True:
                    res.append(grid)
        if last_num == num:
            return res, False
    return res, True
    
class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        if A == 1:
            return ['Q']
        grid = [['B'] * A for jj in range(A)]
        res = []
        res = add_queen(A, res, grid, A, 0)[0]
        for ii in range(len(res)):
            tmp = ''
            for jj in range(len(res[ii])):
                tmp += ''.join(res[ii][jj])
                tmp += ' '
            
            res[ii] = [tmp[:-1]]
        return res

##########################################################################################################################################
