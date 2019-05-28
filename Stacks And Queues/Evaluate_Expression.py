Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Examples:

["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
  
##########################################################################################################################################

class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        ops = set(['+', '-', '*', '/'])
        num = []
        
        ii = 0
        while ii < len(A):
            if A[ii] in ops:
                tmp = eval(A[ii-2] + A[ii] + A[ii-1])
                A[ii-2] = str(tmp)
                B = A[:ii-1]
                B.extend(A[ii+1:])
                A = B
                ii -= 1
            else:
                ii += 1
        return A[0]
            
        
        for ii in range(len(A)):
            if A[ii] in ops:
                num1 = num.pop()
                num2 = num.pop()
                tmp = eval(num2 + A[ii] + num1)
                num.append(str(tmp))
            else:
                num.append(A[ii])
        return num[0]

##########################################################################################################################################
