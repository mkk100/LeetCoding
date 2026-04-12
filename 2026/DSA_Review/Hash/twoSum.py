class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in dictionary:
                return [dictionary[ans], i]
            dictionary[nums[i]] = i
        return []