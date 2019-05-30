# Given an inorder traversal of a cartesian tree, construct the tree.

# Cartesian tree : is a heap ordered binary tree, where the root is greater than all the elements in the subtree. 
# Note: You may assume that duplicates do not exist in the tree. 
# Example :

# Input : [1 2 3]

# Return :   
#           3
#          /
#         2
#        /
#       1
      
##########################################################################################################################################

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

def con_tree(A):
    if len(A) == 1:
        return TreeNode(A[0])
    elif len(A) == 2:
        if A[0] < A[1]:
            node = TreeNode(A[1])
            node.left = TreeNode(A[0])
        else:
            node = TreeNode(A[0])
            node.right = TreeNode(A[1])
        return node
    elif len(A) <= 3:
        if A[0] > A[1] and A[1] > A[2]:
            node = TreeNode(A[0])
            node.right = TreeNode(A[1])
            node.right.right = TreeNode(A[2])
        elif A[0] > A[1] and A[0] < A[2]:
            node = TreeNode(A[2])
            node.left = TreeNode(A[0])
            node.left.right = TreeNode(A[1])
        elif A[0] > A[1] and A[2] > A[1] and A[0] > A[2]:
            node = TreeNode(A[0])
            node.right = TreeNode(A[2])
            node.right.left = TreeNode(A[1])
        elif A[0] < A[1] and A[1] < A[2]:
            node = TreeNode(A[2])
            node.left = TreeNode(A[1])
            node.left.left = TreeNode(A[0])
        else:
            node = TreeNode(A[1])
            node.left = TreeNode(A[0])
            node.right = TreeNode(A[2])
        
        return node
        
        node = TreeNode(A[1])
        node.left = TreeNode(A[0])
        if A[2] > node.val:
            tmp = TreeNode(A[2])
            tmp.left = node
            node = tmp
        else:
            node.right = TreeNode(A[2])
        return node
        
    root = max(A)
    root_idx = A.index(root)
    l = A[0:root_idx]
    r = A[root_idx+1:]
    root = TreeNode(root)
    if len(l) > 0:
        root.left = con_tree(l)
    if len(r) > 0:
        root.right = con_tree(r)
    
    return root

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):
        if len(A) == 0:
            return TreeNode([])
        if len(A) == 1:
            return TreeNode(A[0])
        
        root = max(A)
        root_idx = A.index(root)
        l = A[0:root_idx]
        r = A[root_idx+1:]
        root = TreeNode(root)
        if len(l) > 0:
            root.left = con_tree(l)
        if len(r) > 0:
            root.right = con_tree(r)
        return root
        
##########################################################################################################################################
