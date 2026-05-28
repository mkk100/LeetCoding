class Solution:
    def jump(self, nums: List[int]) -> int:
        res, l, r = 0,0,0
        # we are trying to calculate intervals and how many jumps it takes to get to the end.
        # not so much concern with individual decision trees for each element
        while r < len(nums) - 1: # -1 because last element is where we trying to go to
            farthest = 0
            for i in range(l, r + 1): # right is included
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res

