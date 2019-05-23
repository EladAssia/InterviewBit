You’re given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time 
and constant additional space.

If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Example :

Input : [1 2 3 1 1]
Output : 1 
1 occurs 3 times which is more than 5/3 times. 

##########################################################################################################################################

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        p1 = None
        p2 = None
        for ii in range(len(A)):
            if p1 is not None and A[ii] == p1[0]:
                p1[1] += 1
            elif p2 is not None and A[ii] == p2[0]:
                p2[1] += 1
            elif p1 is None or p1[1] == 0:
                p1 = [A[ii], 1]
            elif p2 is None or p2[1] == 0:
                p2 = [A[ii], 1]
            else:
                p1[1] -= 1
                p2[1] -= 1
        
        c1 = 0
        c2 = 0
        for ii in range(len(A)):
            if p1[0] == A[ii]:
                c1 += 1
            elif p2[0] == A[ii]:
                c2 += 1
        
        if p1 is not None and c1 > float(len(A))/float(3):
            return p1[0]
        if p2 is not None and c2 > float(len(A))/float(3):
            return p2[0]
        return -1

##########################################################################################################################################
