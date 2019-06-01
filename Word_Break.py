Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given

s = "myinterviewtrainer",
dict = ["trainer", "my", "interview"].
Return 1 ( corresponding to true ) because "myinterviewtrainer" can be segmented as "my interview trainer".

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

########################################################################################################################################

class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        if not A:
            return 1
        if not B:
            return 0
        
        s = set()
        max_len = 0
        for ii in B:
            if ii not in s:
                s.add(ii)
                max_len = max(max_len, len(ii))
        
        for ii in range(1, len(A)+1):
            for jj in range(ii-1, ii-max_len-1, -1):
                word1 = A[:jj]
                word2 = A[jj:ii]
                if word1 in s and word2 in s:
                    s.add(A[:ii])
        
        if A in s:
            return 1
        
        return 0
        
########################################################################################################################################
