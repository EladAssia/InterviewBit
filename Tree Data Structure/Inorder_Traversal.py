# Given a binary tree, return the inorder traversal of its nodes’ values.

# Example :
# Given binary tree

#    1
#     \
#      2
#     /
#    3
# return [1,3,2].

# Using recursion is not allowed.

##########################################################################################################################################

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        if A is None:
            return []
        lst = []
        prev = []
        while prev or A.left or A.right:
            # print(A.val)
            if A.left:
                # print('left')
                prev.append(A)
                A = A.left
                continue
            else:
                lst.append(A.val)
                # print(lst)
            
            if A.right:
                # print('right')
                A = A.right
            else:
                if prev:
                    # print('prev')
                    A = prev.pop()
                    # print(A.val)
                # lst.append(A)
                A.left = None
        lst.append(A.val)
        return lst
        
##########################################################################################################################################
