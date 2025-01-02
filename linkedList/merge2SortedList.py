class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
                dummy = dummy.next
            else:
                dummy.next = list2
                list2 = list2.next
                dummy = dummy.next
        
        if list1:
            dummy.next = list1
        elif list2:
            dummy.next = list2
        return tail.next

# time complexity: O(N)
# space complexity: O(1)
# approach: have a tail to return, compare two nodes on each iteration, don't forget to attach the remainders at the back.