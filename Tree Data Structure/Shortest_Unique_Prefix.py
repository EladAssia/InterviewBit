Find shortest unique prefix to represent each word in the list.

Example:

Input: [zebra, dog, duck, dove]
Output: {z, dog, du, dov}
where we can see that
zebra = z
dog = dog
duck = du
dove = dov
NOTE : Assume that no word is prefix of another. In other words, the representation is always possible. 
 
##########################################################################################################################################

import copy


def find_pre(A, n):
    d = {}
    for ii in range(len(A)):
        trim = 0
        if n - 1 > len(A[ii][0]):
            trim = 1
        if A[ii][0][:n - trim] not in d:
            d[A[ii][0][:n - trim]] = [[A[ii][0], ii, A[ii][0][:n - trim]]]
        else:
            d[A[ii][0][:n - trim]].append([A[ii][0], ii, A[ii][0][:n - trim]])

    for k in d:
        if len(d[k]) == 1:
            A[d[k][0][1]][2] = d[k][0][2]
        else:
            d_t = copy.deepcopy(d)
            tmp = find_pre(d[k], n + 1)
            d = d_t
            for ii in range(len(tmp)):
                d[k][ii][2] = tmp[ii][2]
                A[d[k][ii][1]][2] = d[k][ii][2]
    return A
        

class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        d = {}
        for ii in range(len(A)):
            if A[ii][0] not in d:
                d[A[ii][0]] = [[A[ii], ii, A[ii][0]]]
            else:
                d[A[ii][0]].append([A[ii], ii, A[ii][0]])
    
        for k in d:
            if len(d[k]) == 1:
                A[d[k][0][1]] = d[k][0][2]
            else:
                d_t = copy.deepcopy(d)
                tmp = find_pre(d[k], 2)
                d = d_t
                for ii in range(len(tmp)):
                    d[k][ii][2] = tmp[ii][2]
                    A[d[k][ii][1]] = d[k][ii][2]
        return A
        
##########################################################################################################################################
