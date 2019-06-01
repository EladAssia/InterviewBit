# Given an array of integers, find the length of longest subsequence which is first increasing then decreasing.

# **Example: **

# For the given array [1 11 2 10 4 5 2 1]

# Longest subsequence is [1 2 10 4 2 1]

# Return value 6

########################################################################################################################################

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        inc = [1] * len(A)
        dec = [1] * len(A)
        
        for ii in range(len(A)):
            for jj in range(ii):
                if A[ii] > A[jj] and inc[ii] < inc[jj] + 1:
                    inc[ii] = inc[jj] + 1

        for ii in range(len(A) - 2, -1, -1):
            for jj in range(len(A) - 1, ii, -1):
                if A[ii] > A[jj] and dec[ii] < dec[jj] + 1:
                    dec[ii] = dec[jj] + 1
        
        maxx = 0
        for ii in range(len(A)):
            maxx = max(maxx, inc[ii] + dec[ii] - 1)

        return maxx
                    
########################################################################################################################################
