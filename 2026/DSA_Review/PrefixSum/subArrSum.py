class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = {0:1} # prefix sum 0 appears once
        res = 0
        curSum = 0
        for n in nums:
            curSum += n
            res += hashMap.get(curSum - k, 0) 
            hashMap[curSum] = hashMap.get(curSum, 0) + 1
        return res
            