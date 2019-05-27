You are given 3 arrays A, B and C. All 3 of the arrays are sorted.

Find i, j, k such that :
max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))

**abs(x) is absolute value of x and is implemented in the following manner : **

      if (x < 0) return -x;
      else return x;
Example :

Input : 
        A : [1, 4, 10]
        B : [2, 15, 20]
        C : [10, 12]

Output : 5 
         With 10 from A, 15 from B and 10 from C. 
         
##########################################################################################################################################

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        pa, pb, pc = 0, 0, 0
        ans = float('inf')
        while pa < len(A) and pb < len(B) and pc < len(C):
            ans = min(ans, max([abs(A[pa] - B[pb]), abs(A[pa] - C[pc]), abs(B[pb] - C[pc])]))
            
            if A[pa] < B[pb] and A[pa] < C[pc]:
                pa += 1
            elif B[pb] < A[pa] and B[pb] < C[pc]:
                pb += 1
            elif C[pc] < A[pa] and C[pc] < B[pb]:
                pc += 1
            elif A[pa] == B[pb] and A[pa] < C[pc]:
                pa += 1
                pb += 1
            elif A[pa] == C[pc] and A[pa] < B[pb]:
                pa += 1
                pc += 1
            elif B[pb] == C[pc] and B[pb] < A[pa]:
                pb += 1
                pc += 1
            else:
                return 0
        return ans

##########################################################################################################################################
