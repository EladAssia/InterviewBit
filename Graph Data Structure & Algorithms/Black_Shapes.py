Given N * M field of O's and X's, where O=white, X=black
Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)

Example:

OOOXOOO
OOXXOXO
OXOOOXO

answer is 3 shapes are  :
(i)    X
     X X
(ii)
      X
 (iii)
      X
      X
Note that we are looking for connected shapes here.

For example,

XXX
XXX
XXX
is just one single connected black shape.

########################################################################################################################################

def traverse(A, row, col):
    lst = []
    tmp_str = list(A[row])
    tmp_str[col] = 'O'
    A[row] = ''.join(tmp_str)
    lst.append((row, col))
    
    if row > 0 and A[row-1][col] == 'X':
        A, l_t = traverse(A, row-1, col)
        lst.extend(l_t)
    if col < len(A[row]) - 1 and A[row][col+1] == 'X':
        A, l_t = traverse(A, row, col+1)
        lst.extend(l_t)
    if row < len(A) - 1 and A[row+1][col] == 'X':
        A, l_t = traverse(A, row+1, col)
        lst.extend(l_t)
    if col > 0 and A[row][col-1] == 'X':
        A, l_t = traverse(A, row, col-1)
        lst.extend(l_t)
    
    return A, lst
    
    
class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):
        if not A:
            return 0
       
        num = 0
        for row in range(len(A)):
            for col in range(len(A[row])):
                if A[row][col] == 'X':
                    A, lst = traverse(A, row, col)
                    num += 1
        
        return num
        
########################################################################################################################################
