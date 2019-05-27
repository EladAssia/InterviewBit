# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
# Return the sum of the three integers.

# Assume that there will only be one solution

# Example: 
# given array S = {-1 2 1 -4}, 
# and target = 1.

# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)

##########################################################################################################################################

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        n = len(A)
        tot_diff = float('inf')
        for ii in range(len(A)-2):
            jj = ii + 1
            kk = n - 1
            while jj < kk:
                tmp = A[ii] + A[jj] + A[kk]
                diff = abs(tmp - B)
                
                if diff == 0:
                    return tmp
                    
                if diff < tot_diff:
                    tot_diff = diff
                    res = tmp
                
                if res <= B:
                    jj += 1
                else:
                    kk -= 1
        
        return res
    
##########################################################################################################################################
