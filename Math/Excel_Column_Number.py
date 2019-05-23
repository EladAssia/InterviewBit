# Given a column title as appears in an Excel sheet, return its corresponding column number.

# Example:

#     A -> 1
    
#     B -> 2
    
#     C -> 3
    
#     ...
    
#     Z -> 26
    
#     AA -> 27
    
#     AB -> 28 
    
##########################################################################################################################################

class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        col_num = 0
        for ii in range(len(A)):
            col_num += (ord(A[ii])-64)*26**(len(A)-ii-1)
        return col_num

##########################################################################################################################################
