from collections import defaultdict

def detectCycleInDirectedGraph(n, edges):
    def dfs(node):
        visited.add(node)
        path.add(node)

        for neighbour in adj[node]:
            if neighbour not in visited:
                if dfs(neighbour):
                    return True

            elif neighbour in path:
                return True

        path.remove(node)
        return False

        
    visited = set()
    path = set()
    adj = defaultdict(set)

    for a, b in edges:
        adj[a].add(b)

    for i in range(1, n+1):
        if i not in visited and dfs(i):
            return True

    return False
  
