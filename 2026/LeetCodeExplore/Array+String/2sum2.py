class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        hashMap = {}
        
        while l <= r:
            if target - numbers[l] in hashMap:
                return [l + 1, hashMap[target - numbers[l]] + 1]
            if numbers[r] + numbers[l] < target :
                hashMap[numbers[l]] = l
                l += 1
            else:
                hashMap[numbers[r]] = r
                r -= 1
        
# didn't even need hashMap