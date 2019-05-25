# Given two binary strings, return their sum (also a binary string).

# Example:

# a = "100"

# b = "11"
# Return a + b = “111”.

##########################################################################################################################################

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        if not A and not B:
            return ''
        if not A:
            return B
        if not B:
            return A
        A = A[::-1]
        B = B[::-1]
        ans = ''
        rem = '0'
        ii = 0
        while ii < max(len(A), len(B)):
            if ii >= len(A):
                if rem == '1':
                    if B[ii] == '1':
                        ans += '0'
                    else:
                        ans += '1'
                        rem = '0'
                else:
                    ans += B[ii]
            elif ii >= len(B):
                if rem == '1':
                    if A[ii] == '1':
                        ans += '0'
                    else:
                        ans += '1'
                        rem = '0'
                else:
                    ans += A[ii]
            else:
                if A[ii] == '1' and B[ii] == '1' and rem == '1':
                    ans += '1'
                elif A[ii] == '1' and B[ii] == '1':
                    ans += '0'
                    rem = '1'
                elif A[ii] == '1' and rem == '1':
                    ans += '0'
                elif B[ii] == '1' and rem == '1':
                    ans += '0'
                elif A[ii] == '1':
                    ans += '1'
                elif B[ii] == '1':
                    ans += '1'
                elif rem == '1':
                    ans += '1'
                    rem = '0'
                else:
                    ans += '0'
            ii += 1
        if rem == '1':
            ans += '1'
        return ans[::-1]
                
##########################################################################################################################################
