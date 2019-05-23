You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

For example,

A=[1, 3, -1]

f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

So, we return 5.

##########################################################################################################################################

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        
        max1 = -float('inf')
        min1 = float('inf')
        max2 = -float('inf')
        min2 = float('inf')
       
        for ii in range(len(A)): 
            max1 = max(max1, A[ii] + ii) 
            min1 = min(min1, A[ii] + ii) 
            max2 = max(max2, A[ii] - ii) 
            min2 = min(min2, A[ii] - ii) 

        # print('max1={}, min1={}, max2={}, min2={}'.format(max1, min1, max2, min2))
        return max(max1 - min1, max2 - min2) 
     
##########################################################################################################################################
