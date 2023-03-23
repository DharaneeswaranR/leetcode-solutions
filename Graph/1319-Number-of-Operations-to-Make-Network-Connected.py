class Solution:
    # Recursive DFS
    def dfs(self, node, visited, graph):
        for n in graph[node]:
            if not visited[n]:
                visited[n] = True
                self.dfs(n, visited, graph)
                
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # A graph of n nodes require n - 1 edges
        # Return -1 if number of edges(connections) is less than n - 1
        if len(connections) < n - 1:
            return -1 

        graph = defaultdict(list)

        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = [False] * n
        components = 0 # To store number of disconnected graph

        # To find number of disconnected graphs we try to dfs from every node
        # A connected graph require only 1 dfs but a disconnected graph would
        # require multiple dfs (number of disconnected graphs)
        for i in range(n):
            if not visited[i]:
                self.dfs(i, visited, graph)
                components += 1

        # n components require n - 1 edges
        return components - 1