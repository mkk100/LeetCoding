# dfs
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        m, n = len(image), len(image[0])

        def dfs(r, c, original):
            if not (0 <= r < m) or not (0 <= c < n) or image[r][c] != original:
                return
            
            image[r][c] = color
            
            # we moving 4 directions
            dfs(r - 1, c, original)
            dfs(r + 1, c, original)
            dfs(r, c - 1, original)
            dfs(r, c + 1, original)

        dfs(sr, sc, image[sr][sc])
        return image
    

# bfs
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        if orig == color:
            return image
        
        m, n = len(image), len(image[0])
        q = deque([(sr,sc)])
        image[sr][sc] = color
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc  
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == orig:
                    image[nr][nc] = color
                    q.append((nr,nc))
        return image  

