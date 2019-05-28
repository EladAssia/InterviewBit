Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Try solving it using constant additional space.

Example :

Input : 

                  ______
                 |     |
                 \/    |
        1 -> 2 -> 3 -> 4

Return the node corresponding to node 3. 

##########################################################################################################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        if A.next is None:
            return None
        p1, p2 = A, A
        while p2:
            p1 = p1.next
            if p2.next is None:
                return None
            p2 = p2.next
            if p2.next is None:
                return None
            p2 = p2.next
            if p1 == p2:
                break
        
        p1 = A
        while p1:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return A

##########################################################################################################################################
