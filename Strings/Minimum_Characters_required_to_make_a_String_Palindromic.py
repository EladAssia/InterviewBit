You are given a string. The only operation allowed is to insert characters in the beginning of the string. How many minimum characters are needed to be inserted to make the string a palindrome string

Example:
Input: ABC
Output: 2
Input: AACECAAAA
Output: 2

##########################################################################################################################################

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        s = 0
        e = len(A)
        if (s+e)%2 == 0:
            m1 = int((s+e)/2)
            m2 = m1
        else:
            m1 = int((s+e)//2)
            m2 = m1 + 1

        num = 0
        while A[:m1] != A[-1:m2-1:-1]:
            num += 1
            A = A[:-1]
            e -= 1
            if (s+e)%2 == 0:
                m1 = int((s+e)/2)
                m2 = m1
            else:
                m1 = int((s+e)//2)
                m2 = m1 + 1

            if len(A) == 1:
                return num
        
        return num

##########################################################################################################################################
