class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val %= 10

            cur.next = ListNode(val)

            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
            cur = cur.next
        
        return dummy.next

# O(n) time and O(n)
# carry is the key point and a couple edge cases