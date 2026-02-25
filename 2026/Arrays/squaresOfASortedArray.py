# Two Pointers
# We are filling from the back.

# compare the absolute value of the left and right pointers, and insert the larger one 
# to the back of new array. Move the pointer accordingly until they meet.

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        newArr = [0] * n

        left = 0
        right = n - 1
        pos = n - 1

        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                newArr[pos] = nums[right] ** 2
                right -= 1
            else:
                newArr[pos] = nums[left] ** 2
                left += 1
            pos -= 1
        return newArr
