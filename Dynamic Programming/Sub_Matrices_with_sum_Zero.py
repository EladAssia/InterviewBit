Given a 2D matrix, find the number non-empty sub matrices, such that the sum of the elements inside the sub matrix is equal to 0. (note: elements might be negative).

Example:

Input

-8 5  7
3  7 -8
5 -8  9

Output
2

Explanation
-8 5 7
3 7 -8
5 -8 9

-8 5 7
3 7 -8
5 -8 9

########################################################################################################################################

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n, m = len(A), len(A[0]) if A else 0

        if not (n and m):
            return 0

        dp_sum, ans = [[0] * (m + 1) for _ in range(n + 1)], 0

        for ii in range(1, n + 1):
            for jj in range(1, m + 1):
                dp_sum[ii][jj] = dp_sum[ii-1][jj] + dp_sum[ii][jj-1] - dp_sum[ii-1][jj-1] + A[ii-1][jj-1]

        for ii in range(1, n + 1):
            for jj in range(ii, n + 1):
                counti = {0: 1}
                for kk in range(1, m + 1):
                    val = dp_sum[jj][kk] - dp_sum[ii - 1][kk]
                    if val in counti:
                        ans = ans + counti[val]
                        counti[val] = counti[val] + 1
                    else:
                        counti[val] = 1
        return ans
        
########################################################################################################################################
