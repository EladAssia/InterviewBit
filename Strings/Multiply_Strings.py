Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer. 
For example, 
given strings "12", "10", your answer should be “120”.

##########################################################################################################################################

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        # A = A[::-1]
        # B = B[::-1]
        res = [0] * (len(A) + len(B))
        for ii, e1 in enumerate(reversed(A)):
            for jj, e2 in enumerate(reversed(B)):
                res[ii + jj] += int(e1) * int(e2)
                res[ii + jj + 1] += int(res[ii + jj] / 10)
                res[ii + jj] %= 10
        
        while len(res) > 1 and res[-1] == 0: res.pop()
        return ''.join( map(str,res[::-1]) )
        
##########################################################################################################################################
