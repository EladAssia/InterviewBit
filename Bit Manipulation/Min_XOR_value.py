Given an array of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.

Examples : 
Input 
0 2 5 7 
Output 
2 (0 XOR 2) 
Input 
0 4 7 9 
Output 
3 (4 XOR 7)

Constraints: 
2 <= N <= 100 000 
0 <= A[i] <= 1 000 000 000

##########################################################################################################################################

class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        A.sort()
        min_val = float('inf')
        for ii in range(len(A) - 1):
            tmp = (A[ii] | A[ii+1]) - (A[ii] & A[ii+1])
            if tmp < min_val:
                min_val = tmp
            if min_val == 0:
                return 0
        
        return min_val

##########################################################################################################################################
