Given a 2D binary matrix filled with 0’s and 1’s, find the largest rectangle containing all ones and return its area.

Bonus if you can solve it in O(n^2) or less.

Example :

A : [  1 1 1
       0 1 1
       1 0 0 
    ]

Output : 4 

As the max area rectangle is created by the 2x2 rectangle created by (0,1), (0,2), (1,1) and (1,2)

########################################################################################################################################

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, A):
        if len(A) == 1 and len(A[0]) == 1:
            return A[0][0]
        maxx = 0
        lst = [0] * len(A[0])
        for ii in range(len(A)):
            for jj in range(len(A[ii])):
                if A[ii][jj] == 0:
                    lst[jj] = 0
                else:
                    lst[jj] += 1
            s = None
            for jj in range(len(lst)):
                if lst[jj] > 0:
                    if s is None:
                        s = jj
                else:
                    if s is not None:
                        e = jj
                        while s != e:
                            if e == jj:
                                maxx = max(maxx, len(lst[s:e]) * min(lst[s:e]))
                            else:
                                maxx = max(maxx, len(lst[s:e+1]) * min(lst[s:e+1]))
                            if lst[s] < lst[e]:
                                s += 1
                            else:
                                e -= 1
                        maxx = max(maxx, len(lst[s:e+1]) * min(lst[s:e+1]))
                        s = None
            if s is not None:
                e = len(lst)
                while s != e:
                    maxx = max(maxx, len(lst[s:e]) * min(lst[s:e]))
                    if lst[s] < lst[e - 1]:
                        s += 1
                    else:
                        e -= 1

        return maxx
        
########################################################################################################################################
