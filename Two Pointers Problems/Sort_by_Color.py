# Given an array with n objects colored red, white or blue, 
# sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note: Using library sort function is not allowed.

# Example :

# Input : [0 1 2 0 1 2]
# Modify array so that it becomes : [0 0 1 1 2 2]

##########################################################################################################################################

class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        p1, p2 = 0, 1
        while p2 < len(A):
            if A[p1] == 0:
                p1 += 1
            elif A[p2] == 0:
                A[p1], A[p2] = A[p2], A[p1]
                p1 += 1
                p2 += 1
            else:
                p2 += 1
            
            if p2 < p1:
                p2 = p1
        
        p2 = p1
        while p2 < len(A):
            if A[p1] == 1:
                p1 += 1
            elif A[p2] == 1:
                A[p1], A[p2] = A[p2], A[p1]
                p1 += 1
                p2 += 1
            else:
                p2 += 1
            
            if p2 < p1:
                p2 = p1
        return A

##########################################################################################################################################
