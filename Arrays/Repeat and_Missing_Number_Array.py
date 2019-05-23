You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4

##########################################################################################################################################

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        
        A = sorted(list(A))
        d, m = None, None
        for ii in range(1, len(A)):
            if A[ii] == A[ii-1]:
                d = A[ii]
            if A[ii] - 1 != A[ii-1] and A[ii] != A[ii-1]:
                m = A[ii] - 1
        
        if m is None:
            if A[0] == 1:
                m = len(A)
            else:
                m = 1
        return [d, m]

##########################################################################################################################################
