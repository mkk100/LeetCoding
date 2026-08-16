class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        res = float("+inf")
        curSum, l = 0, 0
        # [2, 3, 1, 2, 4, 3, 88], 88 will get it
        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target:
                res = min(res, r - l + 1)
                curSum -= nums[l]
                l += 1
                
        return 0 if math.isinf(res) else res

            
        