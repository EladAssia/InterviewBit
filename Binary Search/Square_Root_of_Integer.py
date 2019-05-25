# Implement int sqrt(int x).

# Compute and return the square root of x.

# If x is not a perfect square, return floor(sqrt(x))

# Example :

# Input : 11
# Output : 3

##########################################################################################################################################

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A == 0:
            return 0
        elif A <= 3:
            return 1
        start = 1
        end = int(A/2)
        while start < end:
            mid = int((start + end) / 2)
            if mid**2 == A:
                return mid
            elif mid**2 > A:
                end = mid - 1
            else:
                start = mid + 1
        
        if mid**2 > A:
            return mid - 1
        else: 
            return mid

##########################################################################################################################################
