class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r- l) // 2)

            if m < len(nums) - 1 and nums[m + 1] > nums[m]:
                l = m + 1
            elif nums[m - 1] > nums[m] and m > 0:
                r = m - 1
            else:
                return m