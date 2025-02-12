class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = -inf
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                answer = max(answer, total)
        return answer
    