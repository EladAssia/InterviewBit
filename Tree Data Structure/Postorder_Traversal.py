# Given a binary tree, return the postorder traversal of its nodes’ values.

# Example :

# Given binary tree

#    1
#     \
#      2
#     /
#    3
# return [3,2,1].

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
    def postorderTraversal(self, root):
        ans = []
        s = []
        tmp = root
        first = True
        while s or first:
            first = False
            l, r = False, False
            while tmp.left:
                s.append(tmp)
                tmp = tmp.left
                l = True
                
            while tmp.right:
                s.append(tmp)
                tmp = tmp.right
                r = True


            if not l and not r:
                prev = tmp
                ans.append(tmp.val)
                tmp = s.pop()
                if tmp.left == prev:
                    tmp.left = None
                elif tmp.right == prev:
                    tmp.right = None

        ans.append(root.val)
        return ans
        
##########################################################################################################################################
