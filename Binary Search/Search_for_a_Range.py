# Given a sorted array of integers, find the starting and ending position of a given target value.

# Your algorithm’s runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example:

# Given [5, 7, 7, 8, 8, 10]

# and target value 8,

# return [3, 4].

##########################################################################################################################################

import math
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        s, e = 0, len(A)-1
        while s < e:
            m = (s+e)//2
            # print('s={}, e={}, m={}'.format(s,e,m))
            if A[m] < B:
                s = m + 1
            elif A[m] > B:
                e = m - 1
            else:
                break
        
        if s > e:
            return [-1, -1]
        elif s == e:
            if A[s] == B:
                return [s, s]
            else:
                return [-1, -1]
        
        if A[s] == B:
            s = 0
        e_s = m
        while s < e_s:
            m_s = (e_s+s)//2
            # print('s={}, e_s={}, m_s={}'.format(s,e_s,m_s))
            if A[m_s] == B:
                e_s = m_s
            else:
                s = m_s + 1
        
        if A[e] == B:
            e = len(A)-1
        s_e = m
        while s_e < e:
            m_e = (s_e+e)//2+1
            if A[m_e] == B:
                s_e = m_e
            else:
                e = m_e - 1
        
        return [s, e]
       
##########################################################################################################################################
