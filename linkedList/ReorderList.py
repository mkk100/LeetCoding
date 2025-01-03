class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        s, f = head, head
        dummy = head

        while f and f.next: # halved linked list
            s = s.next
            f = f.next.next
        
        # reverse second portion
        cur, prev = s.next, None
        s.next = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        cur = head
        sec = prev
        while sec:
            temp1, temp2 = cur.next, sec.next
            cur.next = sec
            sec.next = temp1
            cur,sec = temp1, temp2

# O(N) time complexity, O(1) space complexity: O(1)
# halve a LL using fast and slow ptrs, reverse second portion, and merge two LLs