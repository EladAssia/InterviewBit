# Given an array of integers, every element appears thrice except for one which occurs once.

# Find that element which does not appear thrice.

# Note: Your algorithm should have a linear runtime complexity.

# Could you implement it without using extra memory?

# Example :

# Input : [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
# Output : 4

##########################################################################################################################################

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        A = list(A)
        A.sort()
        for ii in range(0, len(A)-2, 3):
            if A[ii] != A[ii + 1]:
                return A[ii]
        return A[-1]
        
##########################################################################################################################################
