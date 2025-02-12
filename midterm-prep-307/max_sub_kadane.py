class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        i = 0
        total = 0
        while i < len(nums):
            total += nums[i]
            maxSum = max(total, maxSum)
            if total < 0:
                total = 0
            i += 1
        return maxSum
