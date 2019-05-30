Find the lowest common ancestor in an unordered binary tree given two values in the tree.

Lowest common ancestor : the lowest common ancestor (LCA) of two nodes v and w in a tree or directed acyclic graph (DAG) is the lowest (i.e. deepest) node that has both v and w as descendants. 
Example :


        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2_     0        8
         /   \
         7    4
For the above tree, the LCA of nodes 5 and 1 is 3.

LCA = Lowest common ancestor 

Please note that LCA for nodes 5 and 4 is 5.

You are given 2 values. Find the lowest common ancestor of the two nodes represented by val1 and val2
No guarantee that val1 and val2 exist in the tree. If one value doesn’t exist in the tree then return -1.
There are no duplicate values.
You can use extra memory, helper functions, and can modify the node struct but, you can’t add a parent pointer.

##########################################################################################################################################

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

def find_num(A, B, C, l_b, l_c):
    if not l_b or B != l_b[-1]:
        l_b.append(A)
    if not l_c or C != l_c[-1]:
        l_c.append(A)
    
    if A.left:
        l_b, l_c = find_num(A.left, B, C, l_b, l_c)
        if B != l_b[-1]:
            l_b.pop()
        if C != l_c[-1]:
            l_c.pop()
    if A.right:
        l_b, l_c = find_num(A.right, B, C, l_b, l_c)
        if B != l_b[-1]:
            l_b.pop()
        if C != l_c[-1]:
            l_c.pop()
    
    return l_b, l_c
    
    

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        if A is None:
            return -1
        
        l_b, l_c = find_num(A, B, C, [], [])
        if len(l_b) == 1 and l_b[0] != B:
            return -1
        if len(l_c) == 1 and l_c[0] != C:
            return -1
        
        while len(l_b) != len(l_c):
            if len(l_b) > len(l_c):
                l_b.pop()
            else:
                l_c.pop()
        
        while l_b:
            if l_b[-1] == l_c[-1]:
                return l_b[-1]
            
            l_b.pop()
            l_c.pop()
        
##########################################################################################################################################
