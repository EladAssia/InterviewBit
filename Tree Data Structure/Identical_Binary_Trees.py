# Given two binary trees, write a function to check if they are equal or not.

# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

# Return 0 / 1 ( 0 for false, 1 for true ) for this problem

# Example :

# Input : 

#    1       1
#   / \     / \
#  2   3   2   3

# Output : 
#   1 or True
  
##########################################################################################################################################

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        if A is None and B is None:
            return 1
        
        nextA = []
        nextB = []
        
        while nextA or nextB or A.left or A.right or B.left or B.right:
            if A.val != B.val:
                return 0
            
            if A.left and B.left:
                if A.right and B.right:
                    nextA.append(A.right)
                    nextB.append(B.right)
                elif A.right or B.right:
                    return 0
                A = A.left
                B = B.left
                continue
            elif A.left or B.left:
                return 0
            
            if A.right and B.right:
                A = A.right
                B = B.right
                continue
            elif A.right or B.right:
                return 0
            elif nextA:
                A = nextA.pop()
                B = nextB.pop()
        
        if A.val != B.val:
            return 0
        return 1
        
##########################################################################################################################################
