class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        digitCount = 1
        for n in nums:
            while n >= 10:
                n /= 10
                digitCount += 1
            if digitCount % 2 == 0:
                count += 1
            digitCount = 1
        return count

# log is valid approach too, 10^1.5 = 31.62, if you log it, you'll
# get 2 digis, which is what the problem is asking for