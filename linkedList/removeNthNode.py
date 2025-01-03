# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        dummy.next = head
        s, f = dummy, head

        while n > 0 and f:
            f = f.next
            n -= 1
        
        while f:
            s = s.next
            f = f.next
        
        s.next = s.next.next
        return dummy.next

# O(N) for time and O(1) for space
# use fast and slow ptrs.