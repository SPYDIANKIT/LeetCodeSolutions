# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        
        # Find the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Find the node before the nth node from the end
        current = dummy
        for _ in range(length - n):
            current = current.next
        
        # Remove the nth node from the end
        current.next = current.next.next
        
        return dummy.next