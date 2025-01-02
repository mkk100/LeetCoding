class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur, prev = head, None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
# iterative
# Time complexity: O(N)
# Space complexity: O(1)

# recursive
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def reverse(cur, prev):
            if cur is None:
                return prev
            else:
                next = cur.next
                cur.next = prev
                return reverse(next, cur)

        return reverse(head, None)

# Time complexity: O(N)
# Space complexity: O(1) 
# approach: just be careful with the base case.