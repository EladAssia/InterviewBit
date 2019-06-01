# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# For "(()", the longest valid parentheses substring is "()", which has length = 2.

# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

########################################################################################################################################

class Solution:
    # @param A : string
    # @return an integer
    def longestValidParentheses(self, A):
        if len(A) <= 1:
            return 0

        maxx = 0
        lst = [-1]

        for ii in range(len(A)):
            if A[ii] == ')':
                lst.pop()
                if len(lst) != 0:
                    maxx = max(maxx, ii - lst[len(lst) - 1])
                else:
                    lst.append(ii)
            else:
                lst.append(ii)

        return maxx
        
########################################################################################################################################
