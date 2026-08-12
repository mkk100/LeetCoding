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
        k = len(nums1) - 1
        
        while i > 0 or j > 0:
            nums1[k] = nums2[j]
            if nums2[j] > nums1[i]:
                k -= 1
                j -= 1
            else:
                nums1[i],nums1[k] = nums1[k], nums1[i]
                k -= 1
                i -= 1
        
        
# the problem with this approach is that once you finish swapping 

# correct approach

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
        k = len(nums1) - 1
        
        while j >= 0:
            print(nums1[i], nums2[j],nums1[k], nums1)
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i] 
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            
            k -= 1
        

        