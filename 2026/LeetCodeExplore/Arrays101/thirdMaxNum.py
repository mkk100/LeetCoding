class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, second, third = float("-inf") ,float("-inf"), float("-inf")
        
        for n in nums:
            if n > first:
                first, second, third = n, first, second
            elif n < first and n > second:
                second, third = n, second
            elif n < second and n > third:
                third = n
        
        if third == float("-inf"):
            return first
        else:
            return third
                