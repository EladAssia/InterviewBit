Find the longest increasing subsequence of a given sequence / array.

In other words, find a subsequence of array in which the subsequence’s elements are in strictly increasing order, and in which the subsequence is as long as possible. 
This subsequence is not necessarily contiguous, or unique.
In this case, we only care about the length of the longest increasing subsequence.

Example :
Input : [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
Output : 6
The sequence : [0, 2, 6, 9, 13, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15]

########################################################################################################################################

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        lst, ans = [1], 1
        for ii in range(1, len(A)):
            maxx = 1
            for jj in range(ii):
                if A[jj] < A[ii]:
                    maxx = max(maxx, lst[jj] + 1)
            lst.append(maxx)
            ans = max(ans, maxx)
        return ans
        
########################################################################################################################################
