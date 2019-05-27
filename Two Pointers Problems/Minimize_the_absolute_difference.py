Given three sorted arrays A, B and Cof not necessarily same sizes.

Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that a, b, c 
belongs arrays A, B, C respectively.
i.e. minimize | max(a,b,c) - min(a,b,c) |.

Example :

Input:

A : [ 1, 4, 5, 8, 10 ]
B : [ 6, 9, 15 ]
C : [ 2, 3, 6, 6 ]
Output:

1
Explanation: We get the minimum difference for a=5, b=6, c=6 as | max(a,b,c) - min(a,b,c) | = |6-5| = 1.

##########################################################################################################################################

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        min_val = float('inf')
        ida, idb, idc = 0, 0, 0
        while ida < len(A) and idb < len(B) and idc < len(C):
            tmp_min = min(A[ida], B[idb], C[idc])
            tmp_max = max(A[ida], B[idb], C[idc])
            tmp = abs(tmp_max - tmp_min)
            if tmp < min_val: 
                min_val = tmp
            
            if ida < len(A) and A[ida] == tmp_min:
                ida += 1
            elif idb < len(B) and B[idb] == tmp_min:
                idb += 1
            elif idc < len(C) and C[idc] == tmp_min:
                idc += 1
            elif idb + 1 == len(B) and idc + 1 == len(C):
                ida += 1
            elif ida + 1 == len(A) and idc + 1 == len(C):
                idb += 1
            else:
                idc += 1
        
        return min_val

##########################################################################################################################################
