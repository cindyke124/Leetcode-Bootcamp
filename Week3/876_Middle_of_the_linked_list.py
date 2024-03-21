# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        p = head
        number = 0
        while p is not None:
            number += 1
            p = p.next

        count = number / 2

        p = head
        while count > 0:
            p = p.next
            count -= 1
        
        return p

