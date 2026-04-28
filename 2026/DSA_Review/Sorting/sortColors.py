# bucket sort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashMap = {}

        for n in nums:
            hashMap[n] = hashMap.get(n, 0) + 1
        i = 0
        for color in [0,1,2]:
            count = hashMap.get(color, 0)
            for _ in range(count):
                nums[i] = color
                i += 1

# quick sort partition
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l, r = 0, len(nums) - 1
        i = 0
        
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else: 
                i += 1
