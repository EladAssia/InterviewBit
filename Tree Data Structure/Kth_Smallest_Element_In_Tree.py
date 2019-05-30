# Given a binary search tree, write a function to find the kth smallest element in the tree.

# Example :

# Input : 
#   2
#  / \
# 1   3

# and k = 2

# Return : 2

# As 2 is the second smallest element in the tree.
# NOTE : You may assume 1 <= k <= Total number of nodes in BST 
 
##########################################################################################################################################

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
def create_list(A, lst):
    if A.left:
        lst = create_list(A.left, lst)
    lst.append(A.val)
    if A.right:
        lst = create_list(A.right, lst)
    
    return lst
    
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        if A is None:
            return 0
        if not A.left and not A.right:
            return A.val
        lst = []
        lst = create_list(A, lst)
        # print(lst)
        return lst[B-1]

##########################################################################################################################################
