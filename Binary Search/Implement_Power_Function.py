# Implement pow(x, n) % d.

# In other words, given x, n and d,

# find (xn % d)

# Note that remainders on division cannot be negative. 
# In other words, make sure the answer you return is non negative.

# Input : x = 2, n = 3, d = 3
# Output : 2

# 2^3 % 3 = 8 % 3 = 2.

##########################################################################################################################################

class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        
        if n <= 2:
            return x**n%d
        
        ans = 1
        base = x
        while n > 0:
            
            if n%2 == 1:
                ans = ans * base % d
                n -= 1
            else:
                base = base * base % d
                n /= 2
        
        if ans > 0:
            ans = (ans + d) % d
            
        return ans
                
##########################################################################################################################################
