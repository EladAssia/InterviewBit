# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), 
# design an algorithm to find the maximum profit.

# Example :

# Input : [1 2]
# Return :  1

########################################################################################################################################

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if len(A) <= 1:
            return 0
        ans = 0
        tmp_max, tmp_min = A[0], A[0]
        
        for ii in range(1, len(A)):
            if A[ii] > tmp_max:
                tmp_max = A[ii]
            elif A[ii] < tmp_min:
                ans = max(ans, tmp_max - tmp_min)
                tmp_min, tmp_max = A[ii], A[ii]
        
        ans = max(ans, tmp_max - tmp_min)
        return ans
                
########################################################################################################################################
