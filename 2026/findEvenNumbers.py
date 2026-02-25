# First approach: change it to string
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                count += 1
        return count
    

# Second Approach: divide
class Solution(object):
    def evenNumOfDigits(self, num):
        count = 0
        while num > 0:
            num //= 10
            count += 1
        if count % 2 == 0:
            return True
        else:
            return False

    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for n in nums:
            if self.evenNumOfDigits(n):
                count += 1
        return count
        