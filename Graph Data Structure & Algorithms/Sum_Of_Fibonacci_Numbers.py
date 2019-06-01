# How many minimum numbers from fibonacci series are required such that sum of numbers should be equal to a given Number N?
# Note : repetition of number is allowed.

# Example:

# N = 4
# Fibonacci numbers : 1 1 2 3 5 .... so on
# here 2 + 2 = 4 
# so minimum numbers will be 2 

########################################################################################################################################

class Solution:
    # @param A : integer
    # @return an integer
    def fibsum(self, A):
        if not A:
            return 9
        fib = [1, 1]
        while fib[-1] < A:
            fib.append(fib[-1] + fib[-2])
        
        s = set(fib)
        if A in s:
            return 1
        
        minn = float('inf')
        for ii in range(len(fib)-1, -1, -1):
            if fib[ii] > A:
                continue
            rem = A - fib[ii]
            num = 1
            for jj in range(ii, -1, -1):
                if rem < fib[jj]:
                    continue
                rem -= fib[jj]
                num += 1
                if rem == 0:
                    minn = min(minn, num)
        
        return minn
        
########################################################################################################################################
