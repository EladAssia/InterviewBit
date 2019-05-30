Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers % 1003.

Example :

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.

##########################################################################################################################################

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

def path(A, num, lst):
    num += str(A.val)
    
    if A.left:
        lst = path(A.left, num, lst)
    if A.right:
        lst = path(A.right, num, lst)
    
    if not A.left and not A.right:
        lst.append(int(num))
    return lst

class Solution:
    # @param A : root node of tree
    # @return an integer
    def sumNumbers(self, A):
        if not A:
            return 0
        
        lst = path(A, '', [])
        # print(lst)
        return sum(lst)%1003
        
##########################################################################################################################################
