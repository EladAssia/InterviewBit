Given a binary tree, return the preorder traversal of its nodes’ values.

Example :
Given binary tree

   1
    \
     2
    /
   3
return [1,2,3].

Using recursion is not allowed.

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
    def preorderTraversal(self, A):
        
        s = [A]
        ans = [A.val]
        tmp = A
        while s or tmp:
            if tmp.left:
                s.append(tmp.left)
                ans.append(tmp.left.val)
                tmp = tmp.left
            elif tmp.right:
                s.append(tmp.right)
                ans.append(tmp.right.val)
                tmp = tmp.right
            else:
                prev = tmp
                if s:
                    if tmp == s[-1]:
                        s.pop()
                    if s:
                        tmp = s.pop()
                        if prev == tmp.left:
                            tmp.left = None
                        elif prev == tmp.right:
                            tmp.right = None
                    else:
                        tmp = None
                else:
                    tmp = None
        return ans
        
##########################################################################################################################################
