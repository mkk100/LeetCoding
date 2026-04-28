class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        cur_sum = 0
        for i in range(k): # first build up to the window
            cur_sum += nums[i]
        max_average = cur_sum / float(k)
        # second slide the window
        for i in range(k, len(nums)):
            cur_sum += nums[i]
            cur_sum -= nums[i - k]
            max_average = max(max_average, cur_sum / float(k))
        
        return max_average
    
    # don't forget to use float()
        


