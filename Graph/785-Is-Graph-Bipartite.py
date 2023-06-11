class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool: 
        size = len(graph)       
        color = [0] * size

        for node in range(size):
            if color[node] != 0:
                continue
            queue = deque([node])
            color[node] = 1

            while queue:
                popped = queue.popleft()
                for n in graph[popped]:
                    if color[n] == 0:
                        color[n] = -color[popped]
                        queue.append(n)
                    elif color[n] == color[popped]:
                        return False
            
        return True
    
    
"""
Approach: BFS

Color the adjacent nodes in alternate color. If any two adjacent nodes has same color then
the graph is not bipartite.

"""