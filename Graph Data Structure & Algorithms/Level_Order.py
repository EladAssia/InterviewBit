# Given a binary tree, return the level order traversal of its nodes’ values. (ie, from left to right, level by level).

# Example :
# Given binary tree

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:

# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# Also think about a version of the question where you are asked to do a level order traversal of the tree when depth of the tree is 
# much greater than number of nodes on a level.

########################################################################################################################################

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import deque

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        if A is None:
            return []
        
        q = deque([A])
        tmpq = deque()
        lst = [[]]
        while q:
            tmp = q.popleft()
            if tmp.left:
                tmpq.append(tmp.left)
            if tmp.right:
                tmpq.append(tmp.right)
            lst[-1].append(tmp.val)
            if not q:
                q = tmpq
                tmpq = deque()
                lst.append([])
        lst.pop()
        return lst
            
########################################################################################################################################
