class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        return arr == arr[::-1]


# need a better way
