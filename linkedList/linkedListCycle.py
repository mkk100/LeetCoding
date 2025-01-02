class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

# Time complexity: O(n)
# Space complexity: O(1)
# Floyd's Tortoise and Hare algorithm