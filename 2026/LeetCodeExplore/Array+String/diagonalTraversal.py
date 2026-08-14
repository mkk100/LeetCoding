class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
            
        rows, cols = len(mat), len(mat[0])
        curRow, curCol = 0, 0
        res = []
        goingUp = True
        
        while rows * cols != len(res):
            if goingUp:
                while curRow >= 0 and curCol < cols: # bounds
                    res.append(mat[curRow][curCol])
                    curCol += 1
                    curRow -= 1  
                if curCol == cols:
                    curCol -= 1
                    curRow += 2
                else:
                    curRow += 1
                goingUp = False
            else:
                while curCol >= 0 and curRow < rows:
                    res.append(mat[curRow][curCol])
                    curRow += 1
                    curCol -= 1
                if curRow == rows:
                    curCol += 2
                    curRow -= 1
                else:
                    curCol += 1
                goingUp = True
        
        return res

            

        