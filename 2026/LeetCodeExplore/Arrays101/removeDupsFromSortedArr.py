class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        for r in range(len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
        return l + 1