# You are given an array of N integers, A1, A2 ,…, AN and an integer K. Return the of count of distinct numbers in all 
# windows of size K.

# Formally, return an array of size N-K+1 where i’th element in this array contains number of distinct elements in 
# sequence Ai, Ai+1 ,…, Ai+k-1.

# Note:

# If K > N, return empty array.
# For example,

# A=[1, 2, 1, 3, 4, 3] and K = 3

# All windows of size K are

# [1, 2, 1]
# [2, 1, 3]
# [1, 3, 4]
# [3, 4, 3]

# So, we return an array [2, 3, 3, 2].

##########################################################################################################################################

from collections import deque
  
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        if B > len(A):
            return []
        d = {}
        lst = []
        for ii in range(len(A)):
            if ii < B:
                if A[ii] not in d:
                    d[A[ii]] = 1
                else:
                    d[A[ii]] += 1
                continue
    
            lst.append(len(d))
    
            if A[ii] not in d:
                d[A[ii]] = 1
            else:
                d[A[ii]] += 1
    
            d[A[ii - B]] -= 1
            if d[A[ii - B]] == 0:
                del d[A[ii - B]]
    
        lst.append(len(d))
        return lst
            
##########################################################################################################################################
