# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# You need to do this in place.

# Note that if you end up using an additional array, you will only receive partial score.

# Example:

# If the array is

# [
#     [1, 2],
#     [3, 4]
# ]
# Then the rotated array becomes:

# [
#     [3, 1],
#     [4, 2]
# ]

##########################################################################################################################################

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        if not A:
            return []
        n = len(A)-1
        for row in range((n+1) // 2):
            for col in range(row, n-row):
                A[row][col], A[col][n-row], A[n-row][n-col], A[n-col][row] = A[n-col][row], A[row][col], A[col][n-row], A[n-row][n-col]

        return A

##########################################################################################################################################
