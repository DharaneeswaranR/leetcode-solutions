class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()

        def dfs(i, j):
            if 0 <= i < n and 0 <= j < n and grid[i][j] == 1:
                queue.append((i, j))
                grid[i][j] = -1
                dfs(i+1, j)
                dfs(i, j+1)
                dfs(i-1, j)
                dfs(i, j-1)
    
        flag = False
        for i in range(n):
            if flag:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    flag = True
                    break
        
        dist = 0
        while queue:
            bfs = deque()
            for x, y in queue:
                for cur_x, cur_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= cur_x < n and 0 <= cur_y < n:
                        if grid[cur_x][cur_y] == 1:
                            return dist
                        elif grid[cur_x][cur_y] == 0:
                            bfs.append((cur_x, cur_y))
                            grid[cur_x][cur_y] = -1
            
            queue = bfs
            dist += 1

        return dist
    

"""
Approach: BFS and DFS

- Use DFS to mark one of the island as -1 to differntiate it from the other island
- Use BFS to find the shortest distance from the other island to the first island

"""