# Given an array of integers, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2. 
# Please note that your returned answers (both index1 and index2 ) are not zero-based. 
# Put both these numbers in order in an array and return the array from your function 
# (Looking at the function signature will make things clearer). 
# Note that, if no pair exists, return empty list.

# If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the minimum index2, 
# choose the one with minimum index1 out of them.

# Input: [2, 7, 11, 15], target=9
# Output: index1 = 1, index2 = 2

##########################################################################################################################################

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        if len(A) == 0:
            return []
        d = {}
        for ii in range(len(A)):
            if A[ii] not in d:
                d[A[ii]] = [ii]
            else:
                d[A[ii]].append(ii)
        
        ans = []
        for k in d:
            tmp = B - k
            if tmp in d:
                tmp_ans = []
                if tmp == k:
                    if len(d[k]) > 1:
                        tmp_ans = [d[k][0]+1, d[k][1]+1]
                else:
                    tmp_ans = sorted([d[k][0]+1, d[tmp][0]+1])
                
                if len(ans) == 0:
                    ans = tmp_ans
                else:
                    if len(tmp_ans) > 0:
                        if ans[1] > tmp_ans[1]:
                            ans = tmp_ans
                        elif ans[1] == tmp_ans[1] and ans[0] > tmp_ans[0]:
                            ans = tmp_ans
        
        return ans
        
##########################################################################################################################################
