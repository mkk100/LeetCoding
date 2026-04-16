class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        rows = len(matrix)
        l, r = 0, rows - 1
        m = 0
        while l <= r:
            m = (l + (r - l)//2)
            if matrix[m][-1] < target:
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
            else:
                break
        if rows == -1:
            return False
        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[m][mid] > target:
                r = mid - 1
            elif matrix[m][mid] < target:
                l = mid + 1
            else:
                return True
        return False


# o(log m * n)
# there's one other approach that treats the entire matrix as one giant sorted array.