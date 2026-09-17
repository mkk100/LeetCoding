class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        rows, cols = len(image), len(image[0])
        orig = image[sr][sc]
        
        if orig == color:
            return image
        
        def dfs(r,c):
            if (r not in range(rows) or c not in range(cols) or image[r][c] != orig):
                return
            
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        dfs(sr, sc)
        return image
    
# no need for nested loops because it's only asking connected pixels, not every single pixel
# So, it's different from a problem like num of Islands