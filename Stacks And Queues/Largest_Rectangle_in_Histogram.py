Given n non-negative integers representing the histogram’s bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Largest Rectangle in Histogram: Example 1

A histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

Largest Rectangle in Histogram: Example 2

The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.

##########################################################################################################################################

class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        if len(A) == 1:
            return A[0]
        n = len(A)
        ans, ii, tmp = 0, 0, 0
        s = []
        while ii < n:
            if not s or A[s[-1]] <= A[ii]:
                s.append(ii)
                ii += 1
            else:
                top = s.pop()
                if not s:
                    tmp = A[top]*ii
                else:
                    tmp = A[top]*(ii-s[-1]-1)
                ans = max(ans, tmp)
        
        while s:
            top = s.pop()
            if not s:
                tmp = A[top] * ii
            else:
                tmp = A[top]*(ii-s[-1]-1)
            ans = max(ans, tmp)
        return ans

##########################################################################################################################################
