# dfs
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r,c):
            if (r not in range(rows) or 
            c not in range(cols) or grid[r][c] == 0 or
            (r,c) in visit): 
                return 0
            visit.add((r,c))
            return (1 + dfs(r + 1, c) +
            dfs(r - 1, c) +
            dfs(r, c + 1) + 
            dfs(r, c - 1))
            
        area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = max(area, dfs(r, c))
        return area
                
# bfs
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            res = 1

            while q:
                row, col = q.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr in range(rows) and
                    nc in range(cols) and 
                    grid[nr][nc] == 1 and
                    (nr,nc) not in visit):
                        q.append((nr,nc))
                        visit.add((nr,nc))
                        res += 1
            return res


        area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = max(area, bfs(r,c))
        return area              