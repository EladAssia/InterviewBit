Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

########################################################################################################################################

def traverse(A, visited, row, col, curr, found):
    visited.add((row, col))
    # print('row={}, col={}, visited={}'.format(row, col, visited))
    if A[row][col] == 'X':
        return visited, found, curr
    
    
    if row == 0 or row == len(A)-1 or col == 0 or col == len(A[0])-1:
        return visited, False, curr
    
    curr.add((row, col))
    if row > 0 and (row-1, col) not in visited:
        # print('first')
        visited, found, curr = traverse(A, visited, row-1, col, curr, found)
        # if not found:
        #     return visited, found, curr
    if col < len(A[0])-1 and (row, col+1) not in visited:
        # print('second')
        visited, found, curr = traverse(A, visited, row, col+1, curr, found)
        # if not found:
        #     return visited, found, curr
    if row < len(A)-1 and (row+1, col) not in visited:
        # print('third')
        visited, found, curr = traverse(A, visited, row+1, col, curr, found)
        # if not found:
        #     return visited, found, curr
    if col > 0 and (row, col-1) not in visited:
        # print('fourth')
        visited, found, curr = traverse(A, visited, row, col-1, curr, found)
        # if not found:
        #     return visited, found, curr
    
    return visited, found, curr

class Solution:
    # @param A : list of list of chars
    def solve(self, A):
        if not A:
            return []
        visited = set()
        for row in range(1, len(A)-1):
            for col in range(1, len(A[0])-1):
                if (row, col) not in visited:
                    visited.add((row, col))
                    if A[row][col] == 'O':
                        curr = set()
                        visited, found, curr = traverse(A, visited, row, col, curr, True)
                        if found:
                            for ii in curr:
                                A[ii[0]][ii[1]] = 'X'
        
        return A
                    
########################################################################################################################################
