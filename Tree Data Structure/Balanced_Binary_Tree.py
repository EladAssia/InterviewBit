Given a binary tree, determine if it is height-balanced.

Height-balanced binary tree : is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Example :

Input : 
          1
         / \
        2   3

Return : True or 1 

Input 2 : 
         3
        /
       2
      /
     1

Return : False or 0 
         Because for the root node, left subtree has depth 2 and right subtree has depth 0. 
         Difference = 2 > 1. 
         
##########################################################################################################################################

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
def is_bal(A):
    t_l, t_r = 1, 1
    if A.left:
        t_l = is_bal(A.left)
        if t_l is False:
            return t_l
        t_l += 1
    if A.right:
        t_r = is_bal(A.right)
        if t_r is False:
            return t_r
        t_r += 1
    
    if abs(t_l - t_r) > 1:
        return False
    
    return max(t_l, t_r)
    

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        if A is None:
            return 1
        if not A.left and not A.right:
            return 1
        
        ans = is_bal(A)
        if ans: 
            return 1
        return 0
        
##########################################################################################################################################
