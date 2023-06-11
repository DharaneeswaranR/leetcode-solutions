class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
            
        n = len(grid)
        length = 1
        queue = deque([(0, 0)])

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for curr_x, curr_y in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1), (x - 1, y - 1), (x + 1, y + 1), (x -1, y + 1), (x + 1, y - 1)]:
                    if 0 <= curr_x < n and 0 <= curr_y < n:
                        if curr_x == n - 1 and curr_y == n - 1:
                            return length + 1
                        if grid[curr_x][curr_y] == 0:
                            queue.append((curr_x, curr_y))
                            grid[curr_x][curr_y] = 1
            
            length += 1

        return -1