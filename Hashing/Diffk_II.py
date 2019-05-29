# Given an array A of integers and another non negative integer k, find if there exists 2 indices i and j such that 
# A[i] - A[j] = k, i != j.

# Example :

# Input :

# A : [1 5 3]
# k : 2
    
# Output :
# 1

# as 3 - 1 = 2

# Return 0 / 1 for this problem.

##########################################################################################################################################

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
       # print(B)
        if len(A) <= 1:
            return 0
        d = {}
        for ii in A:
            if ii not in d:
                d[ii] = 1
            else:
                d[ii] += 1
        
        # print(d)
        for k in d:
            if B == 0 and d[k] > 1:
                return 1
            elif B == 0:
                continue
            tmp = k + B
            # print('k={}, tmp={}'.format(k, tmp))
            if tmp in d:
                return 1
        return 0

##########################################################################################################################################
