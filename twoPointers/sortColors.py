class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # red = 0 
        # white = 0
        # blue = len(nums) - 1

        # while white <= blue:
        #     if nums[white] == 0:
        #         nums[red], nums[white] = nums[white], nums[red]
        #         red += 1
        #         white += 1
        #     elif nums[white] == 1:
        #         white += 1
        #     else:
        #         nums[white], nums[blue] = nums[blue], nums[white]
        #         blue -= 1
        # return nums

# Duth National Flag Algorithm