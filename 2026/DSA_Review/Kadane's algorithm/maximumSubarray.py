class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            curSum = max(curSum, 0) # we don't take curSum if < 0
            curSum += n
            maxSum = max(maxSum, curSum)
        return maxSum