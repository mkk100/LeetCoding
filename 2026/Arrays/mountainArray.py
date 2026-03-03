# walk up, check peak and walk down and check if we at the end of array.
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        if n < 3:
            return False
        
        i = 0
        
        # walk up
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        
        # peak can't be first or last
        if i == 0 or i == n - 1:
            return False
        
        # walk down
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
        
        return i == n - 1