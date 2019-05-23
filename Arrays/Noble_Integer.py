Given an integer array, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p
If such an integer is found return 1 else return -1.

##########################################################################################################################################

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()

        for ii in range(len(A)):
            if ((ii != len(A)-1 and A[ii] != A[ii + 1]) or (ii == len(A) - 1)) and (A[ii] == len(A) - ii - 1):
                return 1
        
        return -1

##########################################################################################################################################
