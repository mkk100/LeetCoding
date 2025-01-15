# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0, head)
        s, f = head, head.next
        head = f

        while f and f.next:
            print(s.val,f.val)
            t1 = f.next
            f.next = s
            f = t1.next
            s.next = t1
            s = t1

        return head
        