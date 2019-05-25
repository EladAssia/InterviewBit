# N number of books are given. 
# The ith book has Pi number of pages. 
# You have to allocate books to M number of students so that maximum number of pages alloted to a student is minimum. A book will be allocated to exactly one student. Each student has to be allocated at least one book. Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.

# NOTE: Return -1 if a valid assignment is not possible

# Input:

# List of Books
# M number of students
# Your function should return an integer corresponding to the minimum number.

# Example:

# P : [12, 34, 67, 90]
# M : 2

# Output : 113

# There are 2 number of students. Books can be distributed in following fashion : 
#   1) [12] and [34, 67, 90]
#       Max number of pages is allocated to student 2 with 34 + 67 + 90 = 191 pages
#   2) [12, 34] and [67, 90]
#       Max number of pages is allocated to student 2 with 67 + 90 = 157 pages 
#   3) [12, 34, 67] and [90]
#       Max number of pages is allocated to student 1 with 12 + 34 + 67 = 113 pages

# Of the 3 cases, Option 3 has the minimum pages = 113. 

##########################################################################################################################################

def num_of_books(A, m): 
    tot = 0
    num = 1
  
    for ii in A: 
        tot += ii 
        if (tot > m): 
            tot = ii
            num += 1
  
    return num 

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        if len(A) < B:
            return -1
        if len(A) == B:
            return max(A)
            
        tot = sum(A)
        big = max(A)
        while big < tot:
            m = big + (tot-big)//2
            num = num_of_books(A, m)
            if num <= B:
                tot = m
            else:
                big = m + 1
        
        return big

##########################################################################################################################################
