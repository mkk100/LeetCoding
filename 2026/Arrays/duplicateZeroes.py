# I don't even understand this well
# not a well-formed problem
# approach: extended virtual array and sliding window from the back
# j is the extended virtual array index.
# if j < n, then we copy
# if arr[i] == 0, then we set j to 0 as well.

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        zeroes = arr.count(0)
        
        i = n - 1
        j = n + zeroes - 1
        
        while i < j:
            if j < n:
                arr[j] = arr[i]
                
            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = 0
            i -= 1
            j -= 1