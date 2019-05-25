# Write a function to find the longest common prefix string amongst an array of strings.

# Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

# As an example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".

# Given the array of strings, you need to find the longest S which is the prefix of ALL the strings in the array.

# Example:

# Given the array as:

# [

#   "abcdefgh",

#   "aefghijk",

#   "abcefgh"
# ]
# The answer would be “a”.

##########################################################################################################################################

class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        min_chr = float('inf')
        for ii in range(len(A)):
            if len(A[ii]) < min_chr:
                min_chr = len(A[ii])
        
        flag = False
        same = False
        for ii in range(min_chr):
            curr_let = A[0][ii]
            for jj in range(1, len(A)):
                if A[jj][ii] != curr_let:
                    flag = True
                    break
            if flag:
                break
            if ii == min_chr - 1:
                same = True
        if same:        
            return A[0][:ii+1]
        return A[0][:ii]
        
##########################################################################################################################################
