Given A, how many structurally unique BST’s (binary search trees) that store values 1...A?

Example :

Given A = 3, there are a total of 5 unique BST’s.


   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


########################################################################################################################################

class Solution:
    # @param A : integer
    # @return an integer
    def numTrees(self, A):
        if A == 0 or A == 1:
            return 1
        
        num = 1
        for ii in range(2, A+1):
            num *= (ii + A)/ii
        
        return round(num)
        
########################################################################################################################################
