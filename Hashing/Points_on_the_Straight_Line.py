# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

# Sample Input :

# (1, 1)
# (2, 2)
# Sample Output :

# 2
# You will be given 2 arrays X and Y. Each point is represented by (X[i], Y[i])

##########################################################################################################################################

def find_b(x,y,m):
    if y < x:
        b = m*y-x
    else:
        b = y - m*x
    return b
    
    
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, A, B):
        if len(A) < 3:
            return len(A)
        
        # print(A)
        # print(B)
        
        maxx = 0
        for ii in range(len(A)):
            d = {}
            same = 1
            m_len = 0
            for jj in range(ii+1, len(A)):
                x = float(A[ii]) - float(A[jj])
                y = float(B[ii]) - float(B[jj])
                
                if A[ii] == A[jj] and B[ii] == B[jj]:
                    same += 1
                    continue
                if x == 0 and y == 0:
                    string = 'y=x'
                elif x == 0:
                    string = 'x=' + str(A[ii])
                elif y == 0:
                    string = 'y=' + str(B[ii])
                else:
                    if abs(y) < abs(x):
                        m = float(1/(y/x))
                        b = find_b(A[ii],B[ii],m)
                        string = str(m) + 'y=x+' + str(b)
                    else:
                        m = float(y/x)
                        b = find_b(A[ii], B[ii], m)
                        string = 'y=' + str(m) + 'x+' + str(b)
    
                if string not in d:
                    d[string] = list()
                    # d[string].add((A[ii], B[ii]))
                    d[string].append((A[jj], B[jj]))
                else:
                    # d[string].add((A[ii], B[ii]))
                    d[string].append((A[jj], B[jj]))
                if m_len < len(d[string]):
                    m_len = len(d[string])
            maxx = max(maxx, m_len + same)
        return maxx

##########################################################################################################################################
