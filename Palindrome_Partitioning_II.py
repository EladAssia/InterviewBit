Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example : 
Given 
s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

########################################################################################################################################

class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, A):
        dp_p, dp_c = [[False] * len(A) for _ in range(len(A))], list()

        for ii in range(len(A)):
            dp_p[ii][ii] = True

        for ii in range(len(A) - 1):
            dp_p[ii][ii + 1] = A[ii] == A[ii + 1]

        for kk in range(3, len(A) + 1):
            for ii in range(0, len(A) - kk + 1):
                jj = ii + kk - 1
                dp_p[ii][jj] = A[ii] == A[jj] and dp_p[ii + 1][jj - 1]



        for ii in range(len(A)):
            if dp_p[0][ii]:
                dp_c.append(0)
            else:
                tmp = float('INF')
                for jj in range(ii):
                    if dp_p[jj + 1][ii] and dp_c[jj]  < tmp:
                        tmp = dp_c[jj]
                dp_c.append(tmp + 1)

        return dp_c[len(A) - 1]
        
########################################################################################################################################
