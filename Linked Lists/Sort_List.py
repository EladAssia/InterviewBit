Sort a linked list in O(n log n) time using constant space complexity.

Example :

Input : 1 -> 5 -> 4 -> 3

Returned list : 1 -> 3 -> 4 -> 5

##########################################################################################################################################

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None
def merge_sort(A, a_len):
    if a_len > 1:
        ii = 1
        r = A
        while ii <= a_len//2:
            prev = r
            r = r.next
            ii += 1
        if a_len%2 == 0:
            ii -= 1
        prev.next = None
        l = merge_sort(A, a_len//2)
        r = merge_sort(r, ii)
        if l.val < r.val:
            new_A = l
            l = l.next
        else:
            new_A = r
            r = r.next
        tmp = new_A
        while l or r:
            if l is None:
                tmp.next = r
                r = r.next
            elif r is None:
                tmp.next = l
                l = l.next
            elif l.val < r.val:
                tmp.next = l
                l = l.next
            else:
                tmp.next = r
                r = r.next
            tmp = tmp.next
        return new_A
    else:
        return A

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        if A.next is None:
            return A
        tmp = A
        ii = 1
        while tmp:
            ii += 1
            tmp = tmp.next
        ii -= 1
        A = merge_sort(A, ii)
        return A

##########################################################################################################################################
