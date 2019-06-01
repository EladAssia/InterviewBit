# Given a grid of size m * n, lets assume you are starting at (1,1) and your goal is to reach (m,n). At any instance, if you are on 
# (x,y), you can either go to (x, y + 1) or (x + 1, y).

# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# Example :
# There is one obstacle in the middle of a 3x3 grid as illustrated below.

# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.

# Note: m and n will be at most 100. 
 
########################################################################################################################################

def find_path(A, row, col):
    if row == len(A) and col == len(A[0]):
        return 1
    
    num = 0
    if row < len(A) - 1 and A[row+1][col] != 1:
        num += find_path(A, row+1, col)
    if col < len(A[0]) - 1 and A[row][col+1] != 1:
        num += find_path(A, row, col+1)
    
    return num
    
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        if A[0][0] == 1:
            return 0
        return find_path(A, 0, 0)
        
########################################################################################################################################
