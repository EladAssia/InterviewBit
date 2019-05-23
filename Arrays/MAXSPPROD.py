You are given an array A containing N integers. The special product of each ith integer in this array is defined as the product of the following:<ul>

LeftSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (i>j). If multiple A[j]’s are present in multiple positions, the LeftSpecialValue is the maximum value of j. 

RightSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (j>i). If multiple A[j]s are present in multiple positions, the RightSpecialValue is the minimum value of j.

Write a program to find the maximum special product of any integer in the array.

Input: You will receive array of integers as argument to function.

Return: Maximum special product of any integer in the array modulo 1000000007.

Note: If j does not exist, the LeftSpecialValue and RightSpecialValue are considered to be 0.

Constraints 1 <= N <= 10^5 1 <= A[i] <= 10^9

##########################################################################################################################################

class Solution:
    
    def _first_greater(self, A, prev=True):
        stack, ans = list(), [0] * len(A)
        it = range(len(A)) if prev else range(len(A)-1, -1, -1)
        for i in it:
            while stack and A[i] >= A[stack[-1]]:
                stack.pop()
            ans[i] = stack[-1] if stack else 0
            stack.append(i)
        return ans
    
    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        
        left = self._first_greater(A)
        right = self._first_greater(A, prev=False)
        maxx = -float('inf')
        for l, r in zip(left, right):
            maxx = max(l * r, maxx)
        return maxx % 1000000007
        
        for ii in range(len(A) - 2, -1, -1):
            r = 0
            val = 0
            # print('S')
            for jj in range(len(A) - 1, ii, -1):
                # print(str(A[jj]) + ' ' + str(A[ii]))
                if A[jj] > A[ii] and val <= A[jj]:
                    r = jj
                    val = A[jj]
                # elif A[jj] < A[ii]:
                #     break
            if r == 0:
                continue
            
            l = 0
            for jj in range(ii - 1, -1, -1):
                if A[jj] > A[ii]:
                    l = jj
                    break
                elif A[jj] < A[ii]:
                    break
            if r*l > 0:
                return r*l
        return 0

##########################################################################################################################################
