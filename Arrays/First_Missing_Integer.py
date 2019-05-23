Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space.

##########################################################################################################################################

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        A.sort()
        miss = 1
        for ii in range(len(A)):
            if A[ii] == miss:
                miss += 1
        return miss

##########################################################################################################################################
