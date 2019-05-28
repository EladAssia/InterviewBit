# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# Example :

# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

# Rain water trapped: Example 1

# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped.

##########################################################################################################################################

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        ans, l_max, r_max = 0, 0, 0
    
        l = 0
        r = len(A) - 1
        # print(ans)
        while l <= r:
            if A[l] < A[r]:
                if A[l] > l_max:
                    l_max = A[l]
                else:
                    ans = ans + l_max - A[l]
                l += 1
    
            else:
                if A[r] > r_max:
                    r_max = A[r]
                else:
                    ans = ans + r_max - A[r]
                r -= 1
    
        return ans

##########################################################################################################################################
