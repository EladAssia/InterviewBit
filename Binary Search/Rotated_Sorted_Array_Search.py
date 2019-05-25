# Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).

# You are given a target value to search. If found in the array, return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Input : [4 5 6 7 0 1 2] and target = 4
# Output : 0

# NOTE : Think about the case when there are duplicates. Does your current solution work? How does the time complexity change?*

##########################################################################################################################################

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        s = 0
        e = len(A) - 1
        while s < e:
            m = (s+e)//2
            if A[m] > A[m-1] and A[m] > A[m+1]:
                break
            if A[m] > A[s]:
                s = m
            elif A[m] < A[e]:
                e = m

        # print(m)
        if B < A[m] and B >= A[0]:
            s = 0
            e = m
        else:
            s = m + 1
            e = len(A) - 1
        
        # print(s)
        # print(e)
        while s <= e:
            m = (s+e)//2
            if A[m] == B:
                return m
            elif A[m] > B:
                e = m - 1
            else:
                s = m + 1
        
        return -1
        
##########################################################################################################################################
