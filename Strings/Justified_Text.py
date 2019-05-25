# Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line.

# Pad extra spaces ‘ ‘ when necessary so that each line has exactly L characters.
# Extra spaces between words should be distributed as evenly as possible.
# If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
# For the last line of text, it should be left justified and no extra space is inserted between words.

# Your program should return a list of strings, where each string represents a single line.

# Example:

# words: ["This", "is", "an", "example", "of", "text", "justification."]

# L: 16.

# Return the formatted lines as:

# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
#  Note: Each word is guaranteed not to exceed L in length. 
 
##########################################################################################################################################

def add_spaces(l, B, num, space_num):
    rem_space = B - num - space_num
    if len(l) > 1:
        idx = 1
        while rem_space > 0:
            l[idx] += ' '
            rem_space -= 1
            idx += 2
            if idx > len(l) - 1:
                idx = 1
    else:
        l[-1] += ' ' * (B - num)
        
    return l
    
class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
        lst = []
        l = []
        num = 0
        space_num = 0
        for ii in range(len(A)):
            if num + space_num == B:
                lst.append(''.join(l))
                l = []
                l.append(A[ii].strip())
                num = len(A[ii].strip())
                space_num = 0
            elif num + space_num + len(A[ii].strip()) == B:
                l.append(A[ii].strip())
                lst.append(''.join(l))
                l = []
                num = 0
                space_num = 0
            elif num + space_num + len(A[ii].strip()) + 1 > B:
                l = add_spaces(l, B, num, space_num)
                lst.append(''.join(l))
                l = []
                l.append(A[ii].strip())
                num = len(A[ii].strip())
                space_num = 0
                if ii != len(A) - 1:
                    if num + space_num + 1 + len(A[ii+1].strip()) <= B:
                        l.append(' ')
                        space_num += 1
                    else:
                        l = add_spaces(l, B, num, space_num)
                elif ii == len(A) - 1:
                    l[-1] += ' ' * (B - num - space_num)
                    lst.append(''.join(l))
            else:
                l.append(A[ii].strip())
                num += len(A[ii].strip())
                if ii != len(A) - 1:
                    if num + space_num + 1 + len(A[ii+1].strip()) <= B:
                        l.append(' ')
                        space_num += 1
                    else:
                        l = add_spaces(l, B, num, space_num)
                        lst.append(''.join(l))
                        l = []
                        num = 0
                        space_num = 0
                elif ii == len(A) - 1:
                    l[-1] += ' ' * (B - num - space_num)
                    lst.append(''.join(l))
        
        return lst
         
##########################################################################################################################################
