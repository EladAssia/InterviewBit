# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one 
# share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell 
# the stock before you buy again).

# Example :

# Input : [1 2 3]
# Return : 2

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
            elif tmp_max > tmp_min:
                tmp = tmp_max - tmp_min
                ans += tmp
                tmp_min, tmp_max = A[ii], A[ii]
            elif A[ii] < tmp_min:
                tmp = tmp_max - tmp_min
                ans += tmp
                tmp_min, tmp_max = A[ii], A[ii]
        
        tmp = tmp_max - tmp_min
        ans += tmp
        return ans
        
########################################################################################################################################
