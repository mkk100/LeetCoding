class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # better approach for pascal, kind of a trick too.
        # Idk if i would have come up with it during the interview.
        # it's forward approach instead of backward approach
        res = [1]
        for i in range(rowIndex):
            nextRow = [0] * (len(res) + 1) # [[1,2,1], [1,3,3,1]]
            for j in range(len(res)):
                nextRow[j] += res[j] 
                nextRow[j + 1] += res[j]
            res = nextRow
        return res