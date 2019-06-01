# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

# For example:
# A = [2,3,1,1,4], return 1 ( true ).

# A = [3,2,1,0,4], return 0 ( false ).

# Return 0/1 for this problem

########################################################################################################################################

class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
        if len(A) == 0 or len(A) == 1:
            return 1
        ii = 0
        while ii < len(A):
            tmp = A[ii+1:A[ii]+ii+1]
            idx = 0
            maxx = 0
            for jj in range(len(tmp)):
                if jj + tmp[jj] > maxx:
                    maxx = jj + tmp[jj]
                    idx = jj
            if maxx == 0:
                return 0

            ii += idx
            ii += 1
        
        return 1
        
########################################################################################################################################
