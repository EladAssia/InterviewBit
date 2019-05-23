Given a set of digits (A) in sorted order, find how many numbers of length B are possible whose value is less than number C.

NOTE: All numbers can only have digits from the given set. 
Examples:

	Input:
	  0 1 5  
	  1  
	  2  
	Output:  
	  2 (0 and 1 are possible)  

	Input:
	  0 1 2 5  
	  2  
	  21  
	Output:
	  5 (10, 11, 12, 15, 20 are possible)
Constraints:

    1 <= B <= 9, 0 <= C <= 1e9 & 0 <= A[i] <= 9
    
##########################################################################################################################################

from itertools import combinations_with_replacement, product

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        counter = 0
        num_len = len(str(C))
        
        if B > num_len or A == []:
            return 0
        
        elif len(str(C)) == 1:
            for ii in range(len(A)):
                if A[ii] >= C:
                    return ii
            return ii+1
            
        elif B < num_len:
            if B == 1:
                return len(A)
            
            num = len(A) ** B
            if A[0] == 0:
                num -= len(A) ** (B-1)
            return num
        
        elif int(str(C)[0]) < min(A):
            return 0
        
        elif int(str(C)[0]) > max(A):
            num = len(A) ** B
            if A[0] == 0:
                num -= len(A) ** (B-1)
            return num
        
        a = []
        is_smaller = True
        C_str = str(C)
        while len(a) < B and is_smaller:
            if int(C_str[len(a)]) in A:
                tmp = 0
                for ii in range(int(C_str[len(a)])):
                    if len(a) == 0 and ii == 0:
                        continue
                    elif ii in A:
                        tmp += 1
                a.append(tmp)
               
            else:
                tmp = 0
                is_smaller = False
                for ii in range(int(C_str[len(a)]) - 1, -1, -1):
                    if len(a) == 0 and ii == 0:
                        continue
                    elif ii in A:
                        tmp += 1
                        
                if tmp == 0:
                    a.append(0)
                else:
                    a.append(tmp)
        
        # print(a)
        num = 0
        for ii in range(len(a)):
            num += a[ii] * len(A) ** (B-ii-1)
            # print(num)
        
        return num
            
##########################################################################################################################################
