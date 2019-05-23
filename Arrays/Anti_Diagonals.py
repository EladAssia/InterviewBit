Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.

Example:

		
Input: 	

1 2 3
4 5 6
7 8 9

Return the following :

[ 
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]


Input : 
1 2
3 4

Return the following  : 

[
  [1],
  [2, 3],
  [4]
]

##########################################################################################################################################

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        if not A:
            return [[]]
        lst = []
        for row in range(len(A)):
            lst.append([])
            for ii in range(row+1):
                lst[-1].append(A[ii][row-ii])
        
        for row in range(1, len(A)):
            lst.append([])
            for ii in range(row, len(A)):
                lst[-1].append(A[ii][len(A)+row-ii-1])
        return lst

##########################################################################################################################################
