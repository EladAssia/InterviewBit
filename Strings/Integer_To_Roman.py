Given an integer, convert it to a roman numeral, and return a string corresponding to its roman numeral version

Input is guaranteed to be within the range from 1 to 3999.

Example :

Input : 5
Return : "V"

Input : 14
Return : "XIV"
Note : This question has a lot of scope of clarification from the interviewer. 
Please take a moment to think of all the needed clarifications and see the expected response using 
“See Expected Output” For the purpose of this question, https://projecteuler.net/about=roman_numerals has very detailed explanations. 
 
##########################################################################################################################################

class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        ans = ''
        while A > 0:
            if A >= 1000:
                ans += 'M'
                A -= 1000
            elif A >= 900:
                ans += 'CM'
                A -= 900
            elif A >= 500:
                ans += 'D'
                A -= 500
            elif A >= 400:
                ans += 'CD'
                A -= 400
            elif A >= 100:
                ans += 'C'
                A -= 100
            elif A >= 90:
                ans += 'XC'
                A -= 90
            elif A >= 50:
                ans += 'L'
                A -= 50
            elif A >= 40:
                ans += 'XL'
                A -= 40
            elif A >= 10:
                ans += 'X'
                A -= 10
            elif A == 9:
                ans += 'IX'
                A -= 9
            elif A >= 5:
                ans += 'V'
                A -= 5
            elif A == 4:
                ans += 'IV'
                A -= 4
            else:
                ans += 'I'
                A -= 1
        return ans

##########################################################################################################################################
