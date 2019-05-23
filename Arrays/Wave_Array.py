Given an array of integers, sort the array into a wave like array and return it, 
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

Example

Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]
NOTE : If there are multiple answers possible, return [2, 1, 4, 3]
 
##########################################################################################################################################

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        odd = 1
        if len(A)%2 == 0:
            odd = 0
        for ii in range(0, len(A)-odd, 2):
            tmp = A[ii]
            A[ii] = A[ii+1]
            A[ii+1] = tmp
        return A

##########################################################################################################################################
