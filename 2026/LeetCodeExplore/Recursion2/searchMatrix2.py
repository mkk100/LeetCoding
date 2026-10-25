class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows, cols = len(matrix) - 1, len(matrix[0]) - 1
        if not matrix or not matrix[0]:
            return False
        
        def search(colS, colE, rowS, rowE):
            if rowS > rowE or colS > colE:
                return False

            mid_r, mid_c = (rowS + rowE) // 2, (colS + colE) // 2
            pivot = matrix[mid_r][mid_c]

            if target == pivot:
                return True
            if target < pivot:
                return search(colS, colE, rowS, mid_r - 1) or search(colS, mid_c - 1, mid_r, rowE) 
            else:
                return search(colS, colE, mid_r + 1,rowE) or search(mid_c + 1, colE, rowS, mid_r)

        return search(0, cols, 0, rows)