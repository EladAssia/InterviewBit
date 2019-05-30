# Given a binary tree, invert the binary tree and return it. 
# Look at the example for more details.

# Example : 
# Given binary tree

#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7
# invert and return

#      1
#    /   \
#   3     2
#  / \   / \
# 7   6 5   4

##########################################################################################################################################

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
def invert_child(A):
    # print(A.val)
    if A.left is not None:
        A.left = invert_child(A.left)
    if A.right is not None:
        A.right = invert_child(A.right)
    
    A.left, A.right = A.right, A.left
    return A
    
class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, A):
        if A is None:
            return []
        A = invert_child(A)
        return A

##########################################################################################################################################
