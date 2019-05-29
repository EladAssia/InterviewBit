A linked list is given such that each node contains an additional random pointer which could point to any node in the list or NULL.

Return a deep copy of the list.

Example

Given list
   1 -> 2 -> 3

with random pointers going from

  1 -> 3
  2 -> 1
  3 -> 1
  
You should return a deep copy of the list. The returned answer should not contain the same node as the original list, but a copy of them. The pointers in the returned list should not link to any node in the original input list.

##########################################################################################################################################

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return
        tmp = head
        d = {}
        while tmp:
            if tmp not in d:
                d[tmp] = RandomListNode(tmp.label)
                d[tmp].next = None
                d[tmp].random = None
            tmp = tmp.next
        for k in d:
            tmp = k.next
            if tmp:
                d[k].next = d[tmp]
            
            tmp = k.random
            if tmp:
                d[k].random = d[tmp]
        return d[head]
        
##########################################################################################################################################
