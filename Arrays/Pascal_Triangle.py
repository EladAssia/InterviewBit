# Given numRows, generate the first numRows of Pascal’s triangle.

# Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

# Example:

# Given numRows = 5,

# Return

# [
#      [1],
#      [1,1],
#      [1,2,1],
#      [1,3,3,1],
#      [1,4,6,4,1]
# ]

##########################################################################################################################################

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        my_list = []
        for ii in range(0, A):
            tmp_list = []
            for jj in range(0, ii+1):
                if jj == 0 or jj == ii:
                    tmp_list.append(1)
                else:
                    tmp_list.append(my_list[ii-1][jj-1]+my_list[ii-1][jj])
            my_list.append(tmp_list)
        return my_list

##########################################################################################################################################
