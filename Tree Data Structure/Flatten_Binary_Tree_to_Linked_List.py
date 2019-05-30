Given a binary tree, flatten it to a linked list in-place.

Example :
Given


         1
        / \
       2   5
      / \   \
     3   4   6
     
The flattened tree should look like:

   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
Note that the left child of all nodes should be NULL.

##########################################################################################################################################

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def find_path(A, lst):
    lst.append(A.val)
    
    if A.left:
        lst = find_path(A.left, lst)
    if A.right:
        lst = find_path(A.right, lst)
    
    return lst
    
    
class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        if A is None:
            return TreeNode([])
        lst = find_path(A, [])
        
        root = TreeNode(lst[0])
        tmp = root
        for ii in range(1, len(lst)):
            tmp.right = TreeNode(lst[ii])
            tmp = tmp.right
            
        return root
        
##########################################################################################################################################
