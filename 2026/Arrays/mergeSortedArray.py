# if/else condition needs to be in this order because of a specific edge case
# otherwise it's just comparing values from the two arrays and filling in the back of nums1
# and shift ptrs accordingly.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        backPtr = m + n - 1
        
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[backPtr] = nums1[i]
                i -= 1
            else:
                nums1[backPtr] = nums2[j]
                j -= 1
            backPtr -= 1