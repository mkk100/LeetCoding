class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1] * (len(nums))
        
        prefix = 1
        for i in range(len(arr)):
            arr[i] *= prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(arr) -1, -1,-1):
            arr[i] *= postfix
            postfix *= nums[i]
        
        return arr