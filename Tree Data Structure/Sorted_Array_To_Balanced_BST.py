# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# Balanced tree : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every 
# node never differ by more than 1. 
# Example :


# Given A : [1, 2, 3]
# A height balanced BST  : 

#       2
#     /   \
#    1     3

##########################################################################################################################################

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def create_tree(A):
    n = len(A)
    if n == 1:
        return TreeNode(A[0])
    elif n == 2:
        root = TreeNode(A[0])
        root.right = TreeNode(A[1])
    else:
        m = n//2
        
        root = TreeNode(A[m])
        root.left = create_tree(A[:m])
        root.right = create_tree(A[m+1:])
    
    return root


class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        if not A:
            return []
        
        return create_tree(A)

##########################################################################################################################################
