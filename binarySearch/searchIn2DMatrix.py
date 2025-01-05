class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(matrix) - 1
        lenRow = len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][lenRow]:
                l = mid + 1
            else:
                break
        mid = (l + r)//2
        l1, r1 = 0, lenRow
        while l1 <= r1:
            mid1 = (r1 + l1) // 2
            if target < matrix[mid][mid1]:
                r1 = mid1 - 1
            elif target > matrix[mid][mid1]:
                l1 = mid1 + 1
            else:
                return True
        return False
# Search the rows first, and then search individual elements.
# The time complexity is O(log(m) + log(n)) where m is the number of rows and n is the number of elements.
# The space complexity is O(1).