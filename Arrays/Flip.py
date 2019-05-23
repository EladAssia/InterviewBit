# You are given a binary string(i.e. with characters 0 and 1) S consisting of characters S1, S2, …, SN. In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and flip the characters SL, SL+1, …, SR. By flipping, we mean change character 0 to 1 and vice-versa.

# Your aim is to perform ATMOST one operation such that in final string number of 1s is maximised. If you don’t want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

# Notes:

# Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.
# For example,

# S = 010

# Pair of [L, R] | Final string
# _______________|_____________
# [1 1]          | 110
# [1 2]          | 100
# [1 3]          | 101
# [2 2]          | 000
# [2 3]          | 001

# We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].
# Another example,

# If S = 111

# No operation can give us more than three 1s in final string. So, we return empty array [].

##########################################################################################################################################

class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        B = []
        l, r = 0, 1
        p_l, p_r = None, None
        A_c, B_c = 0, 0
        for ii in A:
            if ii == '0':
                A_c += 1
                B.append(1)
            else:
                B_c += 1
                B.append(-1)
        
        ans, l, r, m_l, m_g = [], 0, 0, 0, 0
        for ii in range(len(B)):
            if m_l < B[ii]:
                l = ii+1
                m_l = B[ii]
            else:
                m_l += B[ii]
            if m_l > m_g:
                m_g = m_l
                ans = [l, ii+1]
            # print('l={}, g={}, ans={}'.format(m_l, m_g, ans))

        if m_l > m_g:
            ans = [l, len(B)]
        return ans

##########################################################################################################################################
