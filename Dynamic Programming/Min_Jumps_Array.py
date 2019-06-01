# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# Example :
# Given array A = [2,3,1,1,4]

# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

# If it is not possible to reach the end index, return -1.

########################################################################################################################################

class Solution:
    # @param A : list of integers
    # @return an integer
    def jump(self, A):
        if len(A) == 0:
            return 0
        if len(A) == 1:
            if A[0] == 0:
                return 0
            return 1
        ii = 0
        num = 0
        while ii < len(A):
            if A[ii] + ii >= len(A):
                return num+1
            tmp = A[ii + 1:A[ii]+ii + 1]
            idx = 0
            maxx = 0
            for jj in range(len(tmp)):
                if jj + tmp[jj] > maxx:
                    maxx = jj + tmp[jj]
                    idx = jj
            if maxx == 0:
                return -1
                
            ii += idx
            ii += 1
            num += 1

########################################################################################################################################
