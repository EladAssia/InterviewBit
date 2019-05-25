Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Example :

Input : "XIV"
Return : 14
Input : "XX"
Output : 20

##########################################################################################################################################

class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        ans = 0
        prev = None
        for ii in A:
            # print(ans)
            if ii == 'M':
                ans += 1000
                if prev == 'C':
                    ans -= 200
                prev = 'M'
            elif ii == 'D':
                ans += 500
                if prev == 'C':
                    ans -= 200
                prev = 'D'
            elif ii == 'C':
                ans += 100
                if prev == 'X':
                    ans -= 20
                prev = 'C'
            elif ii == 'L':
                ans += 50
                if prev == 'X':
                    ans -= 20
                prev = 'L'
            elif ii == 'X':
                ans += 10
                if prev == 'I':
                    ans -= 2
                prev = 'X'
            elif ii == 'V':
                ans += 5
                if prev == 'I':
                    ans -= 2
                prev = 'V'
            else:
                ans += 1
                prev = 'I'
        return ans

##########################################################################################################################################
