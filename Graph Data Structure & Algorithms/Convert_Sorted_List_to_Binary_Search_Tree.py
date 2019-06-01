# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# A height balanced BST : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every 
# node never differ by more than 1. 

# Example :
# Given A : 1 -> 2 -> 3
# A height balanced BST  :

#       2
#     /   \
#    1     3
   
########################################################################################################################################

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def create_tree(lst):
    # print(lst)
    if len(lst) == 1:
        return TreeNode(lst[0])
    
    m = int(round(len(lst)/2))
    root = TreeNode(lst[m])
    root.left = create_tree(lst[:m])
    if m < len(lst) - 1:
        root.right = create_tree(lst[m+1:])
    
    return root
class Solution:
    # @param A : head node of linked list
    # @return the root node in the tree
    def sortedListToBST(self, A):
        if A is None:
            return 
        if not A.next:
            return TreeNode(A.val)
        tmp = A
        lst = []
        while tmp:
            lst.append(tmp.val)
            tmp = tmp.next
        
        m = int(round(len(lst)/2))
        root = TreeNode(lst[m])
        root.left = create_tree(lst[:m])
        if m < len(lst) - 1:
            root.right = create_tree(lst[m+1:])
        
        return root
        
########################################################################################################################################
