# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all 
# numbers along its path.

# Note: You can only move either down or right at any point in time. 

# Example :
# Input : 

#     [  1 3 2
#        4 3 1
#        5 6 1
#     ]

# Output : 8
#      1 -> 3 -> 2 -> 1 -> 1
     
########################################################################################################################################

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        n = len(A)
        m = len(A[0])
        cost = [[0 for ii in range(m)] for ii in range(n)]
        
        cost[0][0] = A[0][0]
        
        for ii in range(1, m):
            cost[0][ii] = A[0][ii] + cost[0][ii-1]
        
        for ii in range(1, n):
            cost[ii][0] = A[ii][0] + cost[ii-1][0]
        
        for ii in range(1, m):
            for jj in range(1, n):
                cost[jj][ii] = A[jj][ii] + min(cost[jj-1][ii], cost[jj][ii-1])
        
        return cost[n-1][m-1]
        
########################################################################################################################################
