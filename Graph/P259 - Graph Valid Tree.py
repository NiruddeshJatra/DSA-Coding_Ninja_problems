from os import *
from sys import *
from collections import *
from math import *

def checkgraph(edges, n, m):
    # Empty graph with one node is a tree
    if m == 0:
        return n == 1
    
    # For a graph to be a tree:
    # 1. It must be connected
    # 2. It must have no cycles
    # 3. It must have n-1 edges
    
    # Quick check for edge count
    if m != n-1:
        return False
        
    visited = set()
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    def dfs(node, parent):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True

        return False

    if dfs(0, -1):
        return False

    return len(visited) == n
