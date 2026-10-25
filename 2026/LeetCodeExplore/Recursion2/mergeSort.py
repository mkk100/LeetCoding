class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 1 
        while i < len(nums):
            for j in range(0, len(nums), 2 * i):
                left = nums[j:j + i]
                right = nums[j + i:j + 2 * i]
                nums[j:j + 2 * i] = self.merge(left, right)
            i *= 2
        return nums
    
    def merge(self,l_list, r_list):
        res = []
        i, j = 0, 0
        
        while i < len(l_list) and j < len(r_list):
            if l_list[i] > r_list[j]:
                res.append(r_list[j])
                j += 1
            else:
                res.append(l_list[i])
                i += 1
        res.extend(l_list[i:])
        res.extend(r_list[j:])
        return res