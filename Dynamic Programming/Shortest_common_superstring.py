Given a set of strings. Find the length of smallest string which
has all the strings in the set as substring

Constraints:
1) 1 <= Number of strings <= 18
2) Length of any string in the set will not exceed 100.

Example:
Input: [“abcd”, “cdef”, “fgh”, “de”]
Output: 8 (Shortest string: “abcdefgh”)

########################################################################################################################################

def find_common(A, B):
    if len(A) >= len(B):
        for ii in range(len(B)-1, 0, -1):
            l = len(B[:ii])
            if A[-l:] == B[:ii]:
                return A + B[ii:]
    else:
        for ii in range(len(A)-1, 0, -1):
            if A[ii:] == B[:ii]:
                return A + B[ii:]

    return A+B


class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        if len(A) == 0:
            return 0
        ans = float('inf')
        for ii in range(len(A)):
            tmp = A[ii]
            for jj in range(len(A)):
                if ii == jj:
                    continue
                if tmp in A[jj]:
                    tmp = A[jj]
                elif A[jj] not in tmp:
                    tmp = find_common(tmp, A[jj])
                    if len(tmp) >= ans:
                        break
            ans = min(ans, len(tmp))
        return ans
        
########################################################################################################################################
