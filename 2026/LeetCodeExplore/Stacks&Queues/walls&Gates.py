class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        gates = 0
        rows, cols = len(grid), len(grid[0])
        q, visit = deque(), set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        
        while q:
            row, col = q.popleft()
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr, dc in dirs:
                nr, nc = dr + row, dc + col
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] > 10 and (nr,nc) not in visit:
                    q.append((nr,nc))
                    visit.add((nr,nc))
                    grid[nr][nc] = grid[row][col] + 1 
    

