# Find the intersection of two sorted arrays.
# OR in other words,
# Given 2 sorted arrays, find all the elements which occur in both the arrays.

# Example :

# Input : 
#     A : [1 2 3 3 4 5 6]
#     B : [3 3 5]

# Output : [3 3 5]

# Input : 
#     A : [1 2 3 3 4 5 6]
#     B : [3 5]

# Output : [3 5]

# NOTE : For the purpose of this problem ( as also conveyed by the sample case ), assume that elements that appear more than once in both 
# arrays should be included multiple times in the final output. 
 
##########################################################################################################################################

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        B = list(B)
        C = []
        for ii in range(len(A)):
            if A[ii] in B:
                C.append(A[ii])
                B[B.index(A[ii])] = None
        return C

##########################################################################################################################################
