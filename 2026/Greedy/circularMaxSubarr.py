class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMaxSum, maxSum = 0, nums[0]
        curMinSum, minSum = 0, nums[0] 
        # because of circular array, we put minSum to subtract it from total sum to find the max, check second example
        total = 0

        for num in nums:
            curMaxSum = max(num, curMaxSum + num) # part of Kadane's algorithm
            curMinSum = min(num, curMinSum + num)
            total += num
            maxSum = max(maxSum, curMaxSum)
            minSum = min(minSum, curMinSum)
        
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum # edge case if all elements are neg.