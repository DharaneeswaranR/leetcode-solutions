# BFS Traversal
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = set()
        queue = deque([source])

        while queue:
            v = queue.popleft()
            if v == destination:
                return True
            for vertex in graph[v]:
                if vertex not in visited:
                    queue.append(vertex)
                    visited.add(vertex)
        
        return False

# DFS Recursive
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = set()

        def dfs(curr_vertex):
            if curr_vertex == destination:
                return True
            if curr_vertex not in visited:
                visited.add(curr_vertex)
                for next_vertex in graph[curr_vertex]:
                    if dfs(next_vertex):
                        return True
            return False 
        
        return dfs(source)

# DFS Iterative
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = set()
        stack = deque([source])

        while stack:
            v = stack.pop()
            if v == destination:
                return True
            for vertex in graph[v]:
                if vertex not in visited:
                    stack.append(vertex)
                    visited.add(vertex) 

        return False
