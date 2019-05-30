Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Example :

Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

##########################################################################################################################################

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
def path(A, B, num):
    num += A.val
    
    if not A.left and not A.right and num == B:
        return 1
    
    if A.left:
        ans = path(A.left, B, num)
        if ans:
            return ans
    
    if A.right:
        ans = path(A.right, B, num)
        if ans:
            return ans
    
    return 0
    
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        if not A:
            return 0
            
        return path(A, B, 0)
        
##########################################################################################################################################
