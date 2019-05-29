Given a string s, partition s such that every string of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return
  [
    ["a","a","b"]
    ["aa","b"],
  ]
  
Ordering the results in the answer: Entry i will come before Entry j if :
len(Entryi[0]) < len(Entryj[0]) OR
(len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR
(len(Entryi[0]) == len(Entryj[0]) AND … len(Entryi[k] < len(Entryj[k]))

In the given example,
["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa")

##########################################################################################################################################

def is_poly(A):
    for ii in range(len(A)//2):
        if A[ii] != A[len(A)-1-ii]:
            return False
    return True

def rec_chunk(A):
    new_set = []
    for ii in range(1, len(A)):
        for jj in range(len(A) - 1 - ii, -1, -1):
            if is_poly(A[jj:jj + ii + 1]):
                new_set.append([])
                new_set[-1].extend(A[:jj])
                new_set[-1].append(A[jj:jj + ii + 1])
                if jj != len(A) - 1:
                    new_set[-1].extend(A[jj + ii + 1:])
                res = rec_chunk(A[jj+ii+1:])
                if res:
                    for kk in range(len(res)):
                        new_set.append([])
                        new_set[-1].extend(A[:jj])
                        new_set[-1].append(A[jj:jj + ii + 1])
                        new_set[-1].extend(res[kk])

    return new_set
    
class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        new_set = [list(A)]
        new_set.extend(rec_chunk(A))
        new_set.sort()
        return new_set

##########################################################################################################################################
