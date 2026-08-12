class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        zeroes = arr.count(0) # [1,2,3]
        if zeroes == 0:
            return
        res = [0] * len(arr)
        j = len(arr) - 1
        
        for i in range(len(arr) - zeroes, -1, -1):
            if arr[i] == 0:
                j -= 2
            else:
                res[j] = arr[i]
                j -= 1
        # copy????
        for i in range(len(res)):
            arr[i] = res[i]
                        
# not working, not understand solution, come back