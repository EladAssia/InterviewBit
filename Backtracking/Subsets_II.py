# Given a collection of integers that might contain duplicates, S, return all possible subsets.

# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# The subsets must be sorted lexicographically.

# Example:
# If S = [1,2,2], the solution is:

# [
# [],
# [1],
# [1,2],
# [1,2,2],
# [2],
# [2, 2]
# ]

##########################################################################################################################################

def create_sub(A, lst, l, idx):
    prev = None
    for ii in range(idx+1, len(A)):
        if prev is None or prev != A[ii]:
            l.append(A[ii])
            lst.append(l[:])
            prev = A[ii]
            lst = create_sub(A, lst, l, ii)
            l.pop()
    return lst
        
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        A.sort()
        lst = [[]]
        prev = None
        for ii in range(len(A)):
            if prev is None or prev != A[ii]:
                l = [A[ii]]
                lst.append(l[:])
                prev = A[ii]
                lst = create_sub(A, lst, l, ii)
        return lst

##########################################################################################################################################
