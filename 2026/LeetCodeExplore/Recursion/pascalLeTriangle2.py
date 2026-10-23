class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        row = self.getRow(rowIndex - 1)
        row = [0] + row + [0]
        res = []
        for i in range(len(row) - 1):
            res.append(row[i] + row[i + 1])
        return res
            

# mathy solution
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1] * (rowIndex + 1)
        
        # Helper function to fill the row elements recursively
        def helper(i: int):
            if i > rowIndex:
                return
            # Compute the next combination element based on the previous one
            row[i] = row[i - 1] * (rowIndex - i + 1) // i # based on (n - k + 1)  / k, where n is row and k is column
            helper(i + 1)
            
        helper(1)
        return row
