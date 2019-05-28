# Given an absolute path for a file (Unix-style), simplify it.

# Examples:

# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# Note that absolute path always begin with ‘/’ ( root directory )
# Path will not have whitespace characters.

##########################################################################################################################################

class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        A = list(A)
        if len(A) == 0:
            return '/'
        if A[-1] == '/':
            A.pop()
        lst = []
        skip_num = 0
        dot_num = 0
        last = None
        while A:
            tmp = A.pop()
            if tmp == '.':
                dot_num += 1
                last = tmp
                continue
            elif dot_num == 2:
                skip_num += 1
                dot_num = 0
                continue
            else:
                dot_num = 0
            if skip_num:
                if tmp != '/' or last == '.':
                    last = tmp
                    continue
                skip_num -= 1
            if len(lst) > 0:
                if lst[-1] == '/' and tmp == '/':
                    continue
            elif tmp == '/':
                continue
            lst.append(tmp)
            last = tmp
    
        if lst and lst[-1] == '/':
            lst.pop()
        return '/' + ''.join(lst[::-1])

##########################################################################################################################################
