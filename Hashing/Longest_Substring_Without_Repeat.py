# Given a string, 
# find the length of the longest substring without repeating characters.

# Example:

# The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

# For "bbbbb" the longest substring is "b", with the length of 1.

##########################################################################################################################################

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        d, l = {}, 0
        for ii in range(len(A)):
            if A[ii] in d:
                l = max(l, len(d))
                idx = d[A[ii]]
                key = list(d.keys())
                k = 0
                while k < len(key):
                    if d[key[k]] <= idx:
                        del d[key[k]]
                    k += 1
                d[A[ii]] = ii
            else:
                d[A[ii]] = ii
        l = max(l, len(d))
        return l
        
##########################################################################################################################################
