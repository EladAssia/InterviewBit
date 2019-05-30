# Given a binary tree, find its maximum depth.

# The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.

# NOTE : The path has to end on a leaf node. 
# Example :

#          1
#         /
#        2
# max depth = 2.

##########################################################################################################################################

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
def find_path(A, tmp, maxx):
    if tmp > maxx:
        maxx = tmp
    if A.left:
        tmp += 1
        tmp, maxx = find_path(A.left, tmp, maxx)
        tmp -= 1
    if A.right:
        tmp += 1
        tmp, maxx = find_path(A.right, tmp, maxx)
        tmp -= 1
    
    return tmp, maxx

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxDepth(self, A):
        if A is None:
            return 0
        if A.left is None and A.right is None:
            return 1
        
        tmp, maxx = 1, 1
        tmp, maxx = find_path(A, tmp, maxx)
        return maxx

##########################################################################################################################################
