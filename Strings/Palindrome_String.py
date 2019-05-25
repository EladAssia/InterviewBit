# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Example:

# "A man, a plan, a canal: Panama" is a palindrome.

# "race a car" is not a palindrome.

# Return 0 / 1 ( 0 for false, 1 for true ) for this problem

##########################################################################################################################################

import re
class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        charRe = re.compile(r'[^a-zA-Z0-9.]')
        only_chr = [ii for ii in range(len(A)) if not charRe.search(A[ii])]
        new_A = ''.join(A[ii].lower() for ii in only_chr)
        
        for ii in range(len(new_A)//2):
            if new_A[ii] != new_A[len(new_A)-ii-1]:
                return 0
        return 1
        
##########################################################################################################################################
