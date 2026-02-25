# sliding window is used when
# You’re looking for a longest / shortest subarray
# The problem involves contiguous elements
# You can maintain some property while moving through the array

# Explanation
"""
Example
nums = [1,1,0,1,1,1]

Start:
left = 0
max_len = 0
right = 0 (value = 1)

Window = [1]
length = 0 - 0 + 1 = 1
max_len = 1

right = 1 (value = 1)

Window = [1,1]
length = 1 - 0 + 1 = 2
max_len = 2

right = 2 (value = 0)

We hit a 0 ❌
Window invalid (we only allow 1s)

So:

left = right + 1 = 3

We reset window start.
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        maxCount = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                left = right + 1
            else: 
                maxCount = max(maxCount, right - left + 1)
        return maxCount