Given a 2 * N Grid of numbers, choose numbers such that the sum of the numbers
is maximum and no two chosen numbers are adjacent horizontally, vertically or diagonally, and return it.

Example:

Grid:
	1 2 3 4
	2 3 4 5
so we will choose
3 and 5 so sum will be 3 + 5 = 8

Note that you can choose more than 2 numbers

########################################################################################################################################

def are_ne(a,b):
    if a[1] == b[1]:
        return True
    elif a[1] + 1 == b[1]:
        return True
    elif a[1] - 1 == b[1]:
        return True
    return False

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        if A is None:
            return 0
        if len(A) < 2:
            return 0
        lst = []
        for ii in range(len(A[0])):
            lst.append(max(A[0][ii], A[1][ii]))
        
        incl = 0
        excl = 0
         
        for ii in lst: 
            if excl > incl:
                new_excl = excl
            else:
                new_excl = incl 
            incl = excl + ii
            excl = new_excl 
          
        return (excl if excl>incl else incl) 
            
########################################################################################################################################
