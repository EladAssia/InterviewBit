Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

If there is no solution possible, return -1.

Example :

A : [3 5 4 2]

Output : 2 
for the pair (3, 4)

##########################################################################################################################################

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if len(A) == 0:
            return -1
        B = sorted(enumerate(A), key = lambda x:x[1])
        index_arr = [None] * len(A)
        tmp = 0
        for ii in range(len(A)-1, -1, -1):
            tmp = max(tmp, B[ii][0])
            index_arr[ii] = tmp

        maxx = -1
        for ii in range(len(A)):
            if B[ii][1] <= B[index_arr[ii]][1]: maxx = max(maxx, index_arr[ii] - B[ii][0])
        return maxx

##########################################################################################################################################
