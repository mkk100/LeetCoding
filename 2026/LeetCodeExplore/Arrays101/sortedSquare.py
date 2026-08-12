class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l, r = 0, len(nums) - 1
        arr = [0] * len(nums)
        i = len(nums) - 1
        
        while i >= 0:
            if abs(nums[l]) > abs(nums[r]):
                arr[i] = nums[l] ** 2
                l += 1
            else:
                arr[i] = nums[r] ** 2
                r -= 1
            i -= 1
                
        return arr