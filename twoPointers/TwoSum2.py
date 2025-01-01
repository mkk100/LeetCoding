class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r = 0, len(numbers) - 1

        while l <= r:
            total = numbers[l] + numbers[r] 
            if total > target:
                r -= 1
            elif total < target:
                l += 1
            elif total == target:
                return [l + 1, r + 1]

# Time - O(N)
# Space - O(1)
# There are other approaches, take advantage of the sorted array