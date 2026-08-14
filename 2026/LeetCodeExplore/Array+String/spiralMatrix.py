
        # (00)  (01)  (02)
        # (1,0) (1,1) (12) 
        # (2,0) (2,1) (22)
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        rows, cols = len(matrix), len(matrix[0])
        curRow, curCol = 0,0
        res = []
        hashTable = set()
        def appendToArrAndHashTable(r,c):
            res.append(matrix[r][c])
            hashTable.add(tuple([r,c]))
            
        while len(res) != rows * cols:
            # go all the way right
            while curCol < cols and (curRow, curCol) not in hashTable:
                appendToArrAndHashTable(curRow,curCol)
                curCol += 1  
            curCol -= 1; curRow += 1
                
            # go all the way down
            while curRow < rows and (curRow, curCol) not in hashTable:
                appendToArrAndHashTable(curRow,curCol)
                curRow += 1
            curRow -= 1; curCol -= 1

            # go all the way left
            while curCol >= 0 and (curRow, curCol) not in hashTable:
                appendToArrAndHashTable(curRow,curCol)
                curCol -= 1
            curRow -= 1; curCol += 1
            

            # go all the way up
            while curRow >= 0 and (curRow, curCol) not in hashTable:
                appendToArrAndHashTable(curRow,curCol)
                curRow -= 1
            curRow += 1; curCol += 1
            
        return res
            
                