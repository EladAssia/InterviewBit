# There is a row of seats. Assume that it contains N seats adjacent to each other. There is a group of people who are already seated in 
# that row randomly. i.e. some are sitting together & some are scattered.

# An occupied seat is marked with a character 'x' and an unoccupied seat is marked with a dot ('.')

# Now your target is to make the whole group sit together i.e. next to each other, without having any vacant seat between them in such 
# a way that the total number of hops or jumps to move them should be minimum.

# Return minimum value % MOD where MOD = 10000003

# Example

# Here is the row having 15 seats represented by the String (0, 1, 2, 3, ......... , 14) -

#               . . . . x . . x x . . . x . .

# Now to make them sit together one of approaches is -
#                   . . . . . . x x x x . . . . .

# Following are the steps to achieve this -
# 1 - Move the person sitting at 4th index to 6th index -  
#     Number of jumps by him =   (6 - 4) = 2

# 2 - Bring the person sitting at 12th index to 9th index - 
#     Number of jumps by him = (12 - 9) = 3

# So now the total number of jumps made = 
#     ( 2 + 3 ) % MOD = 
#     5 which is the minimum possible jumps to make them seat together.

# There are also other ways to make them sit together but the number of jumps will exceed 5 and that will not be minimum.

# For example bring them all towards the starting of the row i.e. start placing them from index 0. 
# In that case the total number of jumps will be 
#     ( 4 + 6 + 6 + 9 )%MOD 
#     = 25 which is very costly and not an optimized way to do this movement

########################################################################################################################################

class Solution:
    # @param A : string
    # @return an integer
    def seats(self, A):
        MOD = 10000003
        lst = [ii for ii in range(len(A)) if A[ii] == 'x']
        if len(lst) < 1:
            return 0
        min_lst = min(lst)
        max_lst = max(lst)
        d = {}
        for ii in lst:
            d[ii] = 1
        if len(lst)%2 == 0:
            m = lst[len(lst)//2]
            l_av = m - 1
            r_av = m + 1
            while l_av in d:
                l_av -= 1
            while r_av in d:
                r_av += 1
            left, right = 0, 0
            for ii in range(m-1, min_lst-1, -1):
                if ii in d and ii < l_av:
                    left = left + (l_av - ii)
                    l_av -= 1
            for ii in range(m+1, max_lst+1):
                if ii in d and ii > r_av:
                    right = right + (ii - r_av)
                    r_av += 1
            tot = left + right
            m = lst[len(lst)//2 - 1]
            l_av = m - 1
            r_av = m + 1
            while l_av in d:
                l_av -= 1
            while r_av in d:
                r_av += 1
            left, right = 0, 0
            for ii in range(m-1, min_lst-1, -1):
                if ii in d and ii < l_av:
                    left = left + (l_av - ii)
                    l_av -= 1
            for ii in range(m+1, max_lst+1):
                if ii in d and ii > r_av:
                    right = right + (ii - r_av)
                    r_av += 1
            tot = min(tot, left + right)
        else:
            m = lst[len(lst)//2]
            l_av = m - 1
            r_av = m + 1
            while l_av in d:
                l_av -= 1
            while r_av in d:
                r_av += 1
            left, right = 0, 0
            for ii in range(m-1, min_lst-1, -1):
                if ii in d and ii < l_av:
                    left = left + (l_av - ii)
                    l_av -= 1
            for ii in range(m+1, max_lst+1):
                if ii in d and ii > r_av:
                    right = right + (ii - r_av)
                    r_av += 1
            tot = left + right
        return tot%MOD
        
########################################################################################################################################
