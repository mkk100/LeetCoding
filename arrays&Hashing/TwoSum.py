# we can do Brute force with O(n^2) time complexity and O(1) space complexity

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashSet = {}

        for i, n in enumerate(nums):
            if target - n in hashSet:
                return [hashSet[target - n],i]
            hashSet[n] = i
            
    # Time complexity: O(n)
    # Space complexity: O(n)