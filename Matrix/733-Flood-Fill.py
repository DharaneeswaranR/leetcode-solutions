class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])

        def dfs(i, j, start_color):
            if i < 0 or j < 0 or i == m or j == n or color == image[i][j] or start_color != image[i][j]:
                return 
            image[i][j] = color
            dfs(i, j + 1, start_color)
            dfs(i + 1, j, start_color)
            dfs(i - 1, j, start_color)
            dfs(i, j - 1, start_color)
    
        start_color = image[sr][sc]
        dfs(sr, sc, start_color)

        return image