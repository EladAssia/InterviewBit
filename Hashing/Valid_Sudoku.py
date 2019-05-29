Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx

The Sudoku board could be partially filled, where empty cells are filled with the character ‘.’.

A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
##########################################################################################################################################

def get_square(r, c):
    if r < 3:
        sq = 'U'
    elif r < 6:
        sq = 'M'
    else:
        sq = 'B'
    if c < 3:
        sq += 'L'
    elif c < 6:
        sq += 'C'
    else:
        sq += 'R'
    return sq
    
class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        if len(A) != 9 or len(A[0]) != 9:
            return 0
        d = {'UL': [], 'UC': [], 'UR': [], 'ML': [], 'MC': [], 'MR': [], 'BL': [], 'BC': [], 'BR': []}
        for r in range(len(A)):
            for c in range(len(A[r])):
                if A[r][c] == '.':
                    continue
                k = 'row' + str(r)
                if k not in d:
                    d[k] = [A[r][c]]
                else:
                    d[k].append(A[r][c])
                k = 'col' + str(c)
                if k not in d:
                    d[k] = [A[r][c]]
                else:
                    d[k].append(A[r][c])
                k = get_square(r, c)
                d[k].append(A[r][c])
        
        for k in d:
            if len(set(d[k])) != len(d[k]):
                return 0
        
        return 1
        
##########################################################################################################################################
