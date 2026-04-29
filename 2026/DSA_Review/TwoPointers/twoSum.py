class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in hashMap:
                return [hashMap[ans], i]
            hashMap[nums[i]] = i
        return []
        
            