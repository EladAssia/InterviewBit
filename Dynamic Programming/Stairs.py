You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example :

Input : 3
Return : 3

Steps : [1 1 1], [1 2], [2 1]

########################################################################################################################################

def take_step(A, step, lst, tmp):
    if step == A:
        lst.append([tmp])
        return lst, tmp
    tmp.append(1)
    step += 1
    lst, tmp = take_step(A, step, lst, tmp)
    tmp.pop()
    step -= 1
    if step < A - 1:
        tmp.append(2)
        step += 2
        lst, tmp = take_step(A, step, lst, tmp)
        tmp.pop()
        step -= 2
    
    return lst, tmp

class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        if A == 0 or A == 1:
            return 1
        lst = [None] * (A + 1)
        lst[0] = 1
        lst[1] = 1
        for ii in range(2, A):
            lst[ii] = lst[ii-1] + lst[ii-2]
        return lst[ii-1] + lst[ii-2]
        
########################################################################################################################################
