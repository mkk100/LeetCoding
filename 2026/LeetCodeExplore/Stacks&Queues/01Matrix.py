# non multi source approach
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(mat), len(mat[0])
        
        
        def bfs(r, c):
            q = deque([(r, c)])
            visit = {(r, c)}
            count = 0
            dirs = [(0,1),(0,-1),(1,0),(-1,0)]
            
            while q:
                size = len(q)
                for _ in range(size): # only reason we have this loop is for the count+=1 down there, otherwise no way to tell if one layer is done
                    row, col = q.popleft()
                    for dr, dc in dirs:
                        nr, nc = row + dr, col + dc
                        if (nr in range(rows) and 
                            nc in range(cols) and 
                            (nr, nc) not in visit):
                            if mat[nr][nc] == 0:
                                return count + 1
                            visit.add((nr, nc))
                            q.append((nr, nc))
                count += 1
        
        for r in range(rows):
            for c in range(cols):
                count = 0
                if mat[r][c] == 1:
                    mat[r][c] = bfs(r,c)
        return mat
                    

# multisource chad approach
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(mat), len(mat[0])
        q, visit = deque(), set()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        dist = 0
        while q:
            size = len(q)
            for _ in range(size):
                row, col = q.popleft()
                dirs = [(0,1),(0,-1),(1,0),(-1,0)]
                for dr, dc in dirs:
                    nr, nc = dr + row, dc + col
                    if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == 1 and (nr, nc) not in visit:
                        mat[nr][nc] = dist + 1
                        q.append((nr,nc))
                        visit.add((nr,nc))
            dist += 1
        return mat
                