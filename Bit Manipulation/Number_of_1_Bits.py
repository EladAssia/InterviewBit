Write a function that takes an unsigned integer and returns the number of 1 bits it has.

Example:

The 32-bit integer 11 has binary representation

00000000000000000000000000001011
so the function should return 3.

##########################################################################################################################################

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        counter = 0
        while A:
            if A%2 == 1:
                counter += 1
            A //= 2
        
        return counter

##########################################################################################################################################
