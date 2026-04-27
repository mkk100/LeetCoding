class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] or grid[N - 1][N - 1]:# if the start cell or end cell is blocked. 
            return -1
        q = collections.deque([(0,0,1)])
        visit = set([0,0])
        directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]

        while q:
            row, col,length = q.popleft()
            if row == N - 1 and col == N - 1:
                return length
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (0 <= nr < N and 0 <= nc < N and
                grid[nr][nc] == 0 and (nr,nc) not in visit):
                    q.append((nr,nc,length+1))
                    visit.add((nr,nc))
        return -1

# we don't need two for loops here because unlike island problems, we
# know the starting point.