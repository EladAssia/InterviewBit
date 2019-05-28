# Sort a linked list using insertion sort.

# Example :

# Input : 1 -> 3 -> 2

# Return 1 -> 2 -> 3

##########################################################################################################################################

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        if A.next is None:
            return A
        prev, curr = A, A.next
        # ii = 0
        while curr:
            tmp_c = curr
            if curr.val < prev.val:
                # tmp_c = curr
                # prev.val, curr.val = curr.val, prev.val
                tmp = A
                t_prev = A
                while tmp.val < curr.val:
                    t_prev = tmp
                    tmp = tmp.next
                prev.next = curr.next
                if tmp == t_prev:
                    A = curr    
                else:
                    t_prev.next = curr
                curr.next = tmp
                # ii += 1
            # if ii == 30:
            #     return A
            prev, curr = tmp_c, tmp_c.next
        return A

##########################################################################################################################################
