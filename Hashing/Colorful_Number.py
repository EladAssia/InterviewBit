For Given Number N find if its COLORFUL number or not

Return 0/1

COLORFUL number:

A number can be broken into different contiguous sub-subsequence parts. 
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
Example:

N = 23
2 3 23
2 -> 2
3 -> 3
23 -> 6
this number is a COLORFUL number since product of every digit of a sub-sequence are different. 

Output : 1

##########################################################################################################################################

class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        B = {}
        startA = A
        A = str(A)
        a_len = len(A)
        while A:
            for ii in range(len(A)):
                if int(A[ii]) == 0 or int(A[ii]) == 1 and a_len > 1:
                    return 0
                tmp = int(A)//(10**ii)
                if tmp == int(startA):
                    continue
                tmp = str(tmp)
                if len(tmp) == 1:
                    if tmp not in B:
                        B[tmp] = 0
                    else:
                        return 0

                tmp = list(tmp)
                if len(tmp) > 1:
                    res = 1
                    for jj in range(len(tmp)):
                        res *= int(tmp[jj])
                    
                    res = str(res)
                    if res not in B:
                        B[res] = 0
                    else:
                        return 0
            A = A[1:]
        return 1

##########################################################################################################################################
