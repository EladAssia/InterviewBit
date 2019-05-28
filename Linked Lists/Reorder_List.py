Given a singly linked list
L: L0 → L1 → … → Ln-1 → Ln,
reorder it to:
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

You must do this in-place without altering the nodes’ values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

##########################################################################################################################################

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        if A is None or A.next is None:
            return A
        tmp = A
        ii = 0
        flag = 0
        while tmp:
            ii += 1
            tmp = tmp.next
        if ii%2 == 1:
            ii -= 1
            flag = 1
        tmp = A
        for jj in range(ii//2+flag):
            prev = tmp
            tmp = tmp.next
        prev.next = None
        first, last = tmp, tmp
        while tmp.next:
            tmp = tmp.next
            if tmp.next:
                tmp2 = tmp.next
            else:
                tmp2 = None
            tmp.next = first
            last.next = tmp2
            first = tmp
            tmp = last
        new_A, tmp = A, A
        A = A.next
        while A:
            tmp.next = first
            tmp = tmp.next
            first = first.next
            tmp.next = A
            tmp = tmp.next
            A = A.next
        tmp.next = first
        return new_A

##########################################################################################################################################
