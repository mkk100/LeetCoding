# bfs finds the shortest path, dfs finds a path

# bfs solution
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                dirs = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in dirs:
                    r, c = dr + row, dc + col
                    if ((r,c) not in visited and 
                    r in range(rows) and 
                    c in range(cols) and
                    grid[r][c] == "1"):
                        q.append((r,c))
                        visited.add((r,c))
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands
                    

# dfs recursive solution
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visit = set()
        
        def dfs(r,c):
            if (r not in range(rows) or
                c not in range(cols) or
                (r, c) in visit or
                grid[r][c] != "1"):
                return
            visit.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    islands += 1
                    dfs(r, c)
                    
        return islands
    
# dfs iterative solution, awfully similar to bfs 
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visit = set()
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        def dfs(r,c):
            
            stack = []
            stack.append((r,c))
            visit.add((r,c))
            
            while stack:
                row, col = stack.pop()
                dirs = [(0,1),(0,-1),(1,0),(-1,0)]
                for dr, dc in dirs:
                    nr, nc = dr + row, dc + col
                    if ((nr,nc) not in visit and 
                        nr in range(rows) and 
                        nc in range(cols) and 
                        grid[nr][nc] == "1"):
                        visit.add((nr,nc))
                        stack.append((nr,nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    islands += 1
                    dfs(r,c)
        return islands
            
        