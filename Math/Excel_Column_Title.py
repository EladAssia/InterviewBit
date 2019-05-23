Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    
##########################################################################################################################################

class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        col_let = ''
        while A:
            flag = 0
            mod = A%26
            if mod == 0:
                flag = 1
                mod = 26
            A = int(A/26) - flag
            col_let += chr(mod+64)
        return col_let[::-1]

##########################################################################################################################################
