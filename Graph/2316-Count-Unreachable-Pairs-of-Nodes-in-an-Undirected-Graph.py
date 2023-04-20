class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node, visited, graph, count):
            for n in graph[node]:
                if not visited[n]:
                    visited[n] = True
                    count = dfs(n, visited, graph, count + 1)
            return count if count else 1

        graph = defaultdict(list)
        res = 0

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = [False] * n
        comp_nodes = []

        for i in range(n):
            if not visited[i]:
                comp_nodes.append(dfs(i, visited, graph, 0))

        for i in range(len(comp_nodes)):
            res += comp_nodes[i] * (n - comp_nodes[i])
            n -= comp_nodes[i]
        
        return res

"""
Approach: 

- We will use DFS to find the number of nodes in each connected component.
- The number of unreachable nodes from a component is same for all the nodes in 
  that component.
- The number of unreachable pairs will be the product of the number of nodes 
  in each connected component and the number of nodes in the graph minus the 
  number of nodes in each connected component.

"""