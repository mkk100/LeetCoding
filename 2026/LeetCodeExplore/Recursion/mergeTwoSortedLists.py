# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def merge(list1,list2):
            if not list1:
                return list2
            if not list2:
                return list1
            #[1,2,3], [1,3,4], 
            if list1.val > list2.val: 
                list2.next = merge(list1, list2.next) # [2, 3] 2nd, [3, 4]4th
                return list2
            else: # 1, 1
                list1.next = merge(list1.next, list2) # [2,1] 1st, [3, 3] 3rd,
                return list1
                
        return merge(list1,list2)