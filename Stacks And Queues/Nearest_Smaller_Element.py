# Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

# More formally,

# G[i] for an element A[i] = an element A[j] such that 
#     j is maximum possible AND 
#     j < i AND
#     A[j] < A[i]
    
# Elements for which no smaller element exist, consider next smaller element as -1.

# Example:

# Input : A : [4, 5, 2, 10, 8]
# Return : [-1, 4, -1, 2, 2]

# Example 2:

# Input : A : [3, 2, 1]
# Return : [-1, -1, -1]

##########################################################################################################################################

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        if len(A) == 1:
            return [-1]
        lst = [None] * len(A)
        stack = [A[0]]
        for ii in range(len(A)):
            lst[ii] = -1
            for jj in range(len(stack) - 1, -1, -1):
                if stack[jj] < A[ii]:
                    lst[ii] = stack[jj]
                    break
            while stack and stack[-1] >= A[ii]:
                stack.pop()
            stack.append(A[ii])
        return lst

##########################################################################################################################################
