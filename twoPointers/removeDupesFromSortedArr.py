class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r = 0, 1
        while r < len(nums):
            if nums[l] == nums[r]:
                r += 1
            else:
                nums[l + 1] = nums[r]
                r += 1
                l += 1
        return l + 1
# visit 