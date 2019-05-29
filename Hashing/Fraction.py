# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

# If the fractional part is repeating, enclose the repeating part in parentheses.

# Example :

# Given numerator = 1, denominator = 2, return "0.5"
# Given numerator = 2, denominator = 1, return "2"
# Given numerator = 2, denominator = 3, return "0.(6)"

##########################################################################################################################################

from decimal import *   
class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def fractionToDecimal(self, A, B):
        getcontext().prec = 100
        n = str(A/B)
        print(n)
        return
        if '.' not in n:
            return n
        if 'E' in n:
            e = n.index('E')
            e = n[e:]
            print(e)
        p = n.index('.')+1
        for ii in range(p+1, len(n)):
            flag = True
            s = n[p:ii]
            for jj in range(ii, len(n), len(s)):
                if len(n[jj:jj+len(s)]) == len(s) and n[jj:jj+len(s)] == s:
                    flag = False
                    break
            if flag:
                print(s)
                print(n)
                n = n[:p] + '(' + s + ')'
                return n
        return n[:p+30]

##########################################################################################################################################
