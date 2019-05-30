# Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals the given sum.

# For example:
# Given the below binary tree and sum = 22,

#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

##########################################################################################################################################

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

def path(A, B, lst, l, num):
    num += A.val
    l.append(A.val)
    if A.left is None and A.right is None and num == B:
        # print(l)
        lst.append(l[:])
        # print(lst)
        return lst
    
    if A.left:
        lst = path(A.left, B, lst, l, num)
        l.pop()
    if A.right:
        lst = path(A.right, B, lst, l, num)
        l.pop()
    
    return lst
    
    


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def pathSum(self, A, B):
        
        if not A:
            return []
        
        return path(A, B, [], [], 0)
        # print(lst)
        # return lst

##########################################################################################################################################
