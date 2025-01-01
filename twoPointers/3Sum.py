class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if i > 0 and nums[i - 1] == n:  # *
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[l] + nums[r] + n
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:  # **
                        l += 1
        return res


# Time: O(N^2)
# Space: O(n)
# couple edge cases, what if the first two negative nums are repetitive *
# what if the sorted two sum case is repetitive. **
