# bro i give up
# I persisted yay
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        R, C = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (C + 1) for r in range(R + 1)] # attaching extra 0s to left and top for edge cases

        for r in range(R):
            prefix = 0
            for c in range(C):
                prefix += matrix[r][c]
                above = self.sumMat[r][c + 1] # right above
                self.sumMat[r + 1][c + 1] = prefix + above # one element represent the rectangular sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        prefix = self.sumMat[r2][c1 - 1] # these 4 values are basically corners 
        above = self.sumMat[r1 - 1][c2]
        bottomRight = self.sumMat[r2][c2]
        topLeft = self.sumMat[r1 - 1][c1 - 1]

        return bottomRight - prefix - above + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)