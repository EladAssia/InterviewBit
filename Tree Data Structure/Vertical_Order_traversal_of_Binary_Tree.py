Given a binary tree, return a 2-D array with vertical order traversal of it.
Go through the example and image for more details.

Example :
Given binary tree:

      6
    /   \
   3     7
  / \     \
 2   5     9
returns

[
    [2],
    [3],
    [6 5],
    [7],
    [9]
]


Note : If 2 Tree Nodes shares the same vertical level then the one with lesser depth will come first.

##########################################################################################################################################

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
def traverse(A, nodes, v, d, n):
    if v in nodes:
        nodes[v].append((d, n, A.val))
    else:
        nodes[v] = [(d, n, A.val)]
    
    if A.left:
        nodes, n = traverse(A.left, nodes, v-1, d+1, n+1)
    if A.right:
        nodes, n = traverse(A.right, nodes, v+1, d+1, n+1)
    
    return nodes, n
    
class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def verticalOrderTraversal(self, A):
        if not A:
            return []
        n = 0
        nodes = {0: [(0, n, A.val)]}
        if A.left:
            nodes, n = traverse(A.left, nodes, -1, 1, n+1)
        if A.right:
            nodes, n = traverse(A.right, nodes, 1, 1, n+1)
        # print(nodes)
        k = sorted(list(nodes.keys()))
        ans = [[]]
        for ii in k:
            tmp = sorted(nodes[ii])
            for jj in range(len(tmp)):
                ans[-1].append(tmp[jj][2])
            ans.append([])
        
        ans.pop()
        return ans
        
##########################################################################################################################################
