class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        consecutiveOnes = 0
        maxConsecutiveOnes = 0
        for n in nums:
            if n != 1:
                consecutiveOnes = 0
            else:
                consecutiveOnes += 1
                maxConsecutiveOnes = max(consecutiveOnes, maxConsecutiveOnes)
        return maxConsecutiveOnes
