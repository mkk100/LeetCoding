#initial approach
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                nums[l], nums[r] = nums[r], nums[l]
            r -= 1
        
        res = [x ** 2 for x in nums]
                
        return res
    # failed at this test case: [-5,-3,-2,-1]

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