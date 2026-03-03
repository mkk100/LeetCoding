class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # flows from right to left, the last value is -1 because nth to its right
        max_val_right = -1
        
        for i in range(len(arr)-1, -1, -1):
            current = arr[i]
            arr[i] = max_val_right
            max_val_right = max(max_val_right, current)
        return arr
        