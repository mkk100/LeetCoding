class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, cur_sum = 0, 0
        min_window = float("inf")
        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum >= target:
                min_window = min(min_window, r - l + 1)
                cur_sum -= nums[l]
                l += 1    
        
        return 0 if min_window == float('inf') else min_window
    # need to return to the sliding windows and graphs