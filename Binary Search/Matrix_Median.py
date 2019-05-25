# Given a N cross M matrix in which each row is sorted, find the overall median of the matrix. Assume N*M is odd.

# For example,

# Matrix=
# [1, 3, 5]
# [2, 6, 9]
# [3, 6, 9]

# A = [1, 2, 3, 3, 5, 6, 6, 9, 9]

# Median is 5. So, we return 5.
# Note: No extra memory is allowed.

##########################################################################################################################################

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        while len(A) > 1:
            A[0].extend(A[1])
            del A[1]
        A = sorted(A[0])
        return A[len(A)//2]
            
##########################################################################################################################################
