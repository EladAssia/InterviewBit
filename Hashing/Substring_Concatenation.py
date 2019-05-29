# You are given a string, S, and a list of words, L, that are all of the same length.

# Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening 
# characters.

# Example :

# S: "barfoothefoobarman"
# L: ["foo", "bar"]
# You should return the indices: [0,9].
# (order does not matter).

##########################################################################################################################################

import copy

class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        d = {}
        for ii in B:
            if ii not in d:
                d[ii] = 1
            else:
                d[ii] += 1
    
        str_len = len(B[0])
        tot_len = len(B) * str_len
    
        lst = []
        for ii in range(len(A) - tot_len + 1):
            d_t = copy.deepcopy(d)
            tmp = A[ii:ii+tot_len]
            flag = True
            for jj in range(0, len(tmp), str_len):
                if tmp[jj:jj + str_len] in d:
                    if d_t[tmp[jj:jj + str_len]] != 0:
                        d_t[tmp[jj:jj + str_len]] -= 1
                    else:
                        flag = False
                        break
                else:
                    flag = False
                    break
            if flag:
                lst.append(ii)
    
        return lst

##########################################################################################################################################
