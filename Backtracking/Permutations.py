Given a collection of numbers, return all possible permutations.

Example:

[1,2,3] will have the following permutations:

[1,2,3]
[1,3,2]
[2,1,3] 
[2,3,1] 
[3,1,2] 
[3,2,1]
 
NOTE
No two entries in the permutation sequence should be the same.
For the purpose of this problem, assume that all the numbers in the collection are unique.
##########################################################################################################################################

def rec_per(A):
    if len(A) == 1:
        return A

    tot = []
    for ii in range(len(A)):
        new_A = []
        new_A.append([A[ii]])
        tmp = A[:ii]
        tmp.extend(A[ii + 1:])
        rec = rec_per(tmp)
        for jj in range(len(rec)):
            if type(rec[jj]) is int:
                new_A[-1].append(rec[jj])
            else:
                new_A[-1].extend(rec[jj])
            new_A.append([A[ii]])
        new_A.pop()
        tot.extend(new_A)

    return tot

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        if len(A) == 1:
            return [A]
        tot = rec_per(A)
        return tot

##########################################################################################################################################
