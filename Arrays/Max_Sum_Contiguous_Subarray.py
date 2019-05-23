# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example:

# Given the array [-2,1,-3,4,-1,2,1,-5,4],

# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

# For this problem, return the maximum sum.

##########################################################################################################################################

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):

        ans, tot_sum = 0, 0
        for ii in range(1, len(A)):
            if tot_sum + A[ii] > 0:
                tot_sum += A[ii]
            else:
                tot_sum = 0
            ans = max(ans, tot_sum)
        
        if max(A) < 0:
            ans = max(A)
        
        return ans
        
##########################################################################################################################################
