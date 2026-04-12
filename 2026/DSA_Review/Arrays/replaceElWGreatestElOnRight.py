class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxToRight = -1

        for i in range(len(arr) - 1, -1, -1):
            tmp = arr[i]
            arr[i] = maxToRight
            maxToRight = max(maxToRight, tmp)
        return arr
    
    # backwards