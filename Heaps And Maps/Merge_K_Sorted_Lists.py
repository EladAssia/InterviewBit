# Merge k sorted linked lists and return it as one sorted list.

# Example :

# 1 -> 10 -> 20
# 4 -> 11 -> 13
# 3 -> 8 -> 9
# will result in

# 1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20

##########################################################################################################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        if not A:
            return ListNode([])
        root = A[0]
        for ii in range(1, len(A)):
            lst = A[ii]
            tmp = root
            prev = None
            while lst and tmp:
                # print(lst.val)
                # print('tmp={}, lst={}'.format(tmp.val, lst.val))
                if tmp.val < lst.val:
                    # print('tmp')
                    prev = tmp
                    tmp = tmp.next
                else:
                    # print(lst.val)
                    tmp2 = lst.next
                    lst.next = tmp
                    if tmp == root:
                        root = lst
                        prev = root
                    else:
                        # print('t={},p={},l={}'.format(tmp.val, prev.val, lst.val))
                        prev.next = lst
                        prev = prev.next
                    lst = tmp2
            if lst:
                prev.next = lst
        return root

##########################################################################################################################################
