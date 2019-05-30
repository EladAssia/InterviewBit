Given a binary tree, return the zigzag level order traversal of its nodes’ values. (ie, from left to right, then right to 
left for the next level and alternate between).

Example : 
Given binary tree

    3
   / \
  9  20
    /  \
   15   7
return

[
         [3],
         [20, 9],
         [15, 7]
]

##########################################################################################################################################

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        if A is None:
            return 0
        if A.left is None and A.right is None:
            return [[A.val]]
        
        ans = [[A.val]]
        lst = [A]
        r = True
        while lst:
            # print(ans)
            tmp_lst = []
            ans.append([])
            if r:
                r = False
                while lst:
                    node = lst.pop()
                    if node.right:
                        ans[-1].append(node.right.val)
                        tmp_lst.append(node.right)
                    if node.left:
                        ans[-1].append(node.left.val)
                        tmp_lst.append(node.left)
                lst = tmp_lst
            else:
                r = True
                while lst:
                    node = lst.pop()
                    if node.left:
                        ans[-1].append(node.left.val)
                        tmp_lst.append(node.left)
                    if node.right:
                        ans[-1].append(node.right.val)
                        tmp_lst.append(node.right)
                lst = tmp_lst
        ans.pop()
        return ans
        
##########################################################################################################################################
