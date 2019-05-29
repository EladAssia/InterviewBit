# Given a set of distinct integers, S, return all possible subsets.

# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# Also, the subsets should be sorted in ascending ( lexicographic ) order.
# The list is not necessarily sorted.
# Example :

# If S = [1,2,3], a solution is:

# [
#   [],
#   [1],
#   [1, 2],
#   [1, 2, 3],
#   [1, 3],
#   [2],
#   [2, 3],
#   [3],
# ]

##########################################################################################################################################

def rec_sub(A, empty):
    if len(A) == 1:
        return [A]

    new_set = []
    if empty:
        new_set = [[]]

    new_set.append([A[0]])
    res = rec_sub(A[1:], False)
    for ii in range(len(res)):
        new_set.append([A[0]])
        new_set[-1].extend(res[ii])

    new_set.extend(res)
    return new_set

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A.sort()
        if len(A) == 0:
            return [[]]
        if len(A) == 1:
            return [[], [A[0]]]
            
        return rec_sub(A, True)

##########################################################################################################################################
