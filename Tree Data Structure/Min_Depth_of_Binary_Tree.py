Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

NOTE : The path has to end on a leaf node. 
Example :

         1
        /
       2
min depth = 2.

##########################################################################################################################################

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
def find_min(A, tmp, minn):
    if A.left:
        tmp += 1
        tmp, minn = find_min(A.left, tmp, minn)
        tmp -= 1
    if A.right:
        tmp += 1
        tmp, minn = find_min(A.right, tmp, minn)
        tmp -= 1
    
    if tmp < minn and A.left is None and A.right is None:
        minn = tmp
    
    return tmp, minn
    
    
class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, A):
        if A is None:
            return 0
        if A.left is None and A.right is None:
            return 1
        
        tmp, minn = 1, float('inf')
        tmp, minn = find_min(A, tmp, minn)
        
        return minn
        
##########################################################################################################################################
