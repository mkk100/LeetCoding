class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftSum, rightSum = [0] * len(nums), [0] * len(nums)
        leftTotal, rightTotal = 0,0
        
        for i in range(len(nums) - 1, -1, -1):
            rightTotal += nums[i]
            rightSum[i] = rightTotal

        for i in range(len(nums)):
            leftTotal += nums[i]
            leftSum[i] = leftTotal
            if leftSum[i] == rightSum[i]:
                return i
            

        return -1
    

# optimal
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - leftSum - nums[i] 
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
            
        return -1