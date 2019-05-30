# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# Example :

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# The above binary tree is symmetric. 
# But the following is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem

##########################################################################################################################################

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
def traverse(l, r):
    if l.val != r.val:
        return 0
    
    if l.left and r.right:
        ans = traverse(l.left, r.right)
        if ans == 0:
            return 0
    elif l.left is not None and r.right is None:
        return 0
    elif l.left is None and r.right is not None:
        return 0
    
    if l.right and r.left:
        ans = traverse(l.right, r.left)
        if ans == 0:
            return 0
    elif l.right is not None and r.left is None:
        return 0
    elif l.right is None and r.left is not None:
        return 0
    
    return 1
    
class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        if not A:
            return 1
        
        if A.left and A.right:
            ans = traverse(A.left, A.right)
            if ans == 0:
                return 0
        elif A.left is not None and A.right is None:
            return 0
        elif A.left is None and A.right is not None:
            return 0
        
        return 1
            
            
        q = [A]
        d, ii = 1, 0
        tmp_q = []
        lst = []
        while q:
            tmp = q.pop(0)
            if tmp is None:
                tmp_q.append(None)
                tmp_q.append(None)
                ii += 2
            else:
                flag = True
                if tmp.left:
                    tmp_q.append(tmp.left)
                    lst.append((ii, tmp.left.val))
                else:
                    tmp_q.append(None)
                ii += 1
                if tmp.right:
                    tmp_q.append(tmp.right)
                    lst.append((ii, tmp.right.val))
                else: 
                    tmp_q.append(None)
                ii += 1
            if not q:
                # print(lst)
                if flag:
                    q = tmp_q[:]
                    tmp_q = []
                    for ii in range(len(lst)//2):
                        if lst[ii][0] + lst[len(lst)-ii-1][0] != 2**d-1:
                            return 0
                        elif lst[ii][1] != lst[len(lst)-ii-1][1]:
                            return 0
                    lst = []
                    d += 1
                    ii = 0
                flag = False
        return 1        
            
##########################################################################################################################################
