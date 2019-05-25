Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.

[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

##########################################################################################################################################

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        s = 0
        e = len(A)
        
        if A[-1] < B:
            return len(A)
        
        while s <= e:
            m = (s+e)/2
            if A[m] == B:
                return m
            elif A[m] < B:
                s = m + 1
            else:
                e = m - 1
        
        if s > B:
            return B - 1
        return s
            
##########################################################################################################################################
