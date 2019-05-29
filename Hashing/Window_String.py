Given a string S and a string T, find the minimum window in S which will contain all the characters in T in linear time complexity.
Note that when the count of a character C in T is N, then the count of C in minimum window in S should be at least N.

Example :

S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC"

 Note:
If there is no such window in S that covers all characters in T, return the empty string ''.
If there are multiple such windows, return the first occurring minimum window ( with minimum start index ).

##########################################################################################################################################

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def minWindow(self, A, B):
        d = {}
        tot = len(B)
        for ii in range(len(B)):
            if B[ii] not in d:
                d[B[ii]] = 1
            else:
                d[B[ii]] += 1
    
        p1 = 0
        p2 = 0
        pnts = None
        while p2 < len(A) or tot == 0:
    
            if tot == 0:
                if A[p1] in d:
                    if pnts is None:
                        pnts = (p1, p2 - 1)
                    elif pnts[1] - pnts[0] > p2 - p1 - 1:
                        pnts = (p1, p2 - 1)
                    d[A[p1]] += 1
                    if d[A[p1]] == 1:
                        tot += 1
                    p1 += 1
                else:
                    p1 += 1
            else:
                if A[p2] in d:
                    if d[A[p2]] > 0:
                        tot -= 1
                    d[A[p2]] -= 1
    
                p2 += 1
    
        if pnts is None:
            return ''
        return A[pnts[0]:pnts[1]+1]

##########################################################################################################################################
