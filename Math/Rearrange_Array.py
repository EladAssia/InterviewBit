Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

Example:

Input : [1, 0]
Return : [0, 1]
Lets say N = size of the array. Then, following holds true :
All elements in the array are in the range [0, N-1]
N * N does not overflow for a signed integer

##########################################################################################################################################

class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        for ii in range(len(A)):
            if type(A[A[ii]]) is str:
                A[ii] = str(A[ii]) + ',' + str.split(A[A[ii]], ',')[0]
            else:
                A[ii] = str(A[ii]) + ',' + str(A[A[ii]])

        for ii in range(len(A)):
            A[ii] = int(str.split(A[ii], ',')[1])

##########################################################################################################################################
