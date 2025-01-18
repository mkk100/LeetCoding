def maxSubArray(self, nums: List[int]) -> int:

        ans = -inf
        for i in range(len(nums)):
            cur = 0
            for j in range(i, len(nums)):
                cur += nums[j]
                ans = max(cur, ans)
        return ans
        