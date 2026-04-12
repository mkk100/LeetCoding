class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                maxCount = max(count, maxCount)
                count = 0
            else:
                count += 1
        return max(count, maxCount)