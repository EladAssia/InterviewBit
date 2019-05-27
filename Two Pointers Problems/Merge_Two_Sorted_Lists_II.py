Given two sorted integer arrays A and B, merge B into A as one sorted array.

 Note: You have to modify the array A to contain the merge of A and B. Do not output anything in your code.
TIP: C users, please malloc the result into a new array and return the result. 
If the number of elements initialized in A and B are m and n respectively, the resulting size of array A after your code is executed should be m + n

Example :

Input : 
         A : [1 5 8]
         B : [6 9]

Modified A : [1 5 6 8 9]

##########################################################################################################################################

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        idx1, idx2 = 0, 0
        C = []
        while idx1 < len(A) and idx2 < len(B):
            if A[idx1] < B[idx2]:
                C.append(str(A[idx1]))
                idx1 += 1
            else:
                C.append(str(B[idx2]))
                idx2 += 1
        
        if idx1 == len(A):
            for ii in range(idx2, len(B)):
                C.append(str(B[ii]))
        else:
            for ii in range(idx1, len(A)):
                C.append(str(A[ii]))
        A = ' '.join(C)
        A += ' '
        print(A)

##########################################################################################################################################
