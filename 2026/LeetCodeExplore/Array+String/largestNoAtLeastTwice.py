class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, second = [0,float("-inf")], [0,float("-inf")]
        
        for i in range(len(nums)):
            if nums[i] > first[1]:
                first, second = [i,nums[i]], [first[0],first[1]]
            elif nums[i] < first[1] and nums[i] > second[1]:
                second = [i,nums[i]]
        
        if second[1] * 2 <= first[1]:
            return first[0]
        else:
            return -1
# my first approach

#optimal
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxIndex, m = 0, float("-inf")
        for i in range(len(nums)):
            if nums[i] > m:
                maxIndex = i
                m = nums[i]
        
        for n in nums:
            if n == nums[maxIndex]: continue
            if n * 2 > nums[maxIndex]:
                return -1
        return maxIndex
        