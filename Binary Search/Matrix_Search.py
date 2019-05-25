# Write an efficient algorithm that searches for a value in an m x n matrix.

# This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than or equal to the last integer of the previous row.
# Example:

# Consider the following matrix:

# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return 1 ( 1 corresponds to true )

# Return 0 / 1 ( 0 if the element is not present, 1 if the element is present ) for this problem

##########################################################################################################################################

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        c_len = len(A[0])-1
        s, e, m = 0, len(A)-1, None
        while s <= e:
            m_r = (e+s)//2
            if m is not None and m == m_r:
                break
            # print('s={},e={},m_r={},res={}'.format(s, e, m_r,A[m_r][0]))
            if A[m_r][0] > B:
                e = m_r - 1
            elif A[m_r][c_len] < B:
                s = m_r + 1
            else:
                break
            m = m_r
        
        s, e, m = 0, c_len, None
        while s <= e:
            m_c = (e+s)//2
            if m is not None and m == m_c:
                return 0
            # print('s={},e={},m_c={},res={}'.format(s, e, m_c,A[m_r][m_c]))
            if A[m_r][m_c] < B:
                s = m_c + 1
            elif A[m_r][m_c] > B:
                e = m_c - 1
            else:
                return 1
            m = m_c
        return 0
        

##########################################################################################################################################
