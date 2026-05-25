# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        s,f = head, head
        p = None
        while f and f.next:
            f = f.next.next
            tmp = s.next
            s.next = p
            p = s
            s = tmp
        res = 0
        while s:
            res = max(res, s.val + p.val)
            s = s.next
            p = p.next
        return res
