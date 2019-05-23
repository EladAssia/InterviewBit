Determine whether an integer is a palindrome. Do this without extra space.

A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
Negative numbers are not palindromic.

Example :

Input : 12121
Output : True

Input : 123
Output : False

##########################################################################################################################################

class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        A = str(A)
        for ii in range(int(len(A)/2)):
            if A[ii] != A[len(A)-ii-1]:
                return 0
        return 1

##########################################################################################################################################
