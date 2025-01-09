class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, 1
        k = 0
        for r in range(len(nums)):
            if nums[r] == val:
                r += 1
            else:
                nums[l] = nums[r] 
                l += 1
                k += 1
        return k