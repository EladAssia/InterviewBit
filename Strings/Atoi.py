# Implement atoi to convert a string to an integer.

# Example :

# Input : "9 2704"
# Output : 9
# Note: There might be multiple corner cases here. Clarify all your doubts using “See Expected Output”.

#  Questions: Q1. Does string contain whitespace characters before the number?
# A. Yes Q2. Can the string have garbage characters after the number?
# A. Yes. Ignore it. Q3. If no numeric character is found before encountering garbage characters, what should I do?
# A. Return 0. Q4. What if the integer overflows?
# A. Return INT_MAX if the number is positive, INT_MIN otherwise. 
# Warning : DO NOT USE LIBRARY FUNCTION FOR ATOI.
# If you do, we will disqualify your submission retroactively and give you penalty points.

##########################################################################################################################################

import sys
class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        A = A.split(' ')[0]
        s = ord(A[0])-48
        if s < 0 or s > 9:
            if s != -3 and s != -5:
                return 0
        if s == -5:
            s, e = 1, 1
            if len(A) > 1:
                if ord(A[1]) - 48 > 9 or ord(A[1]) - 48 < 0:
                    return 0
        else:
            s, e = 0, 0
        for ii in range(s+1, len(A)):
            tmp = ord(A[ii]) - 48
            if tmp >= 0 and tmp <= 9:
                e = ii
            else:
                if s == e:
                    if s == 0 and A[0] == '-':
                        return 0
                if int(A[s:e+1]) > 2147483647:
                    return 2147483647
                elif int(A[s:e+1]) < -2147483648:
                    return -2147483648
                return int(A[s:e+1])
                
        if e == 0 and A[0] == '-':
            return 0
        if s == 1 and e == 1 and len(A) == 1:
            return 0
        if int(A[s:e+1]) > 2147483647:
            return 2147483647
        elif int(A[s:e+1]) < -2147483648:
            return -2147483648
        return int(A[s:e+1])
        
##########################################################################################################################################
