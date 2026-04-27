class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh, minutes = 0, 0
        m, n = len(grid), len(grid[0])

        for r in range(m): # prep work before BFS
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))

        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh:
            for i in range(len(q)): # extra loop to pop the preexisting oranges
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh -= 1

            minutes += 1
        return minutes if fresh == 0 else -1


