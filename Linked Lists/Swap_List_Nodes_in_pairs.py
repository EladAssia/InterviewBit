Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

##########################################################################################################################################

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        curr = A
        prev = A
        ii = 0
        nextt = None
        prevv = None
        first = True
        while curr:
            if curr.next is not None:
                curr = curr.next
                if curr.next is not None:
                    nextt = curr.next
                else:
                    nextt = None
            else:
                return A
            if curr:
                curr.next = prev
                prev.next = nextt
                if first:
                    A = curr
                    first = False
                if prevv is not None:
                    prevv.next = curr
                
                prevv = prev
                curr = nextt
                prev = nextt
        return A

##########################################################################################################################################
