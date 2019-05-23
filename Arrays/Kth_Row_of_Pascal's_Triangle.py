# Given an index k, return the kth row of the Pascal’s triangle.

# Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

# Example:

# Input : k = 3

# Return : [1,3,3,1]

# NOTE: k is 0 based. k = 0, corresponds to the row [1]. 
# Note: Could you optimize your algorithm to use only O(k) extra space?

##########################################################################################################################################

class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        if A == 0:
            return [1]
        
        my_list = []
        for ii in range(0, A+1):
            tmp_list = []
            for jj in range(0, ii+1):
                if jj == 0 or jj == ii:
                    tmp_list.append(1)
                else:
                    tmp_list.append(my_list[ii-1][jj-1]+my_list[ii-1][jj])
            my_list.append(tmp_list)
        
        return tmp_list

##########################################################################################################################################
