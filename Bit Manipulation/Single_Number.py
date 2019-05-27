Given an array of integers, every element appears twice except for one. Find that single one.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example :

Input : [1 2 2 3 1]
Output : 3

##########################################################################################################################################

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        A = list(A)
        A.sort()
        if len(A) == 1:
            return A[0]
        for ii in range(1, len(A) - 1, 2):
            if ((A[ii-1] | A[ii]) - (A[ii-1] & A[ii])) == 0:
                continue
            elif ((A[ii] | A[ii+1]) - (A[ii] & A[ii+1])) == 0:
                return A[ii-1]
            else:
                return A[ii]
        
        return A[-1]

##########################################################################################################################################
