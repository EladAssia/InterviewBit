# A long array A[] is given to you. There is a sliding window of size w which is moving from the very left of the array to the 
# very right. You can only see the w numbers in the window. Each time the sliding window moves rightwards by one position. 
# You have to find the maximum for each window. The following example will give you more clarity.

# Example :

# The array is [1 3 -1 -3 5 3 6 7], and w is 3.

# Window position	Max
 	 
# [1 3 -1] -3 5 3 6 7	3
# 1 [3 -1 -3] 5 3 6 7	3
# 1 3 [-1 -3 5] 3 6 7	5
# 1 3 -1 [-3 5 3] 6 7	5
# 1 3 -1 -3 [5 3 6] 7	6
# 1 3 -1 -3 5 [3 6 7]	7
# Input: A long array A[], and a window width w
# Output: An array B[], B[i] is the maximum value of from A[i] to A[i+w-1]
# Requirement: Find a good optimal way to get B[i]

#  Note: If w > length of the array, return 1 element with the max of the array.
 
##########################################################################################################################################

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        if B >= len(A):
            return [max(A)]
        
        q = [(A[0], 0)]
        for ii in range(1, B):
            while q and q[-1][0] < A[ii]:
                q.pop()
            q.append((A[ii], ii))
        ans = [q[0][0]]
        for ii in range(B, len(A)):
            while q and q[-1][0] < A[ii]:
                q.pop()
            q.append((A[ii], ii))
            if q[0][1] <= ii - B:
                q.pop(0)
            ans.append(q[0][0])
        return ans

##########################################################################################################################################
