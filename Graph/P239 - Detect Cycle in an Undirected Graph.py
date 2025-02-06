from collections import defaultdict

def readGraph(edgeCount):
	edges = []
	for i in range(edgeCount):
		a, b = map(int, input().split())
		edges.append((a, b))

	return edges


def createAdjList(edges):
	adj = defaultdict(set)
	for a, b in edges:
		adj[a].add(b)
		adj[b].add(a)

	return adj


def dfs(visited, adj, parent, cur):
	visited.add(cur)

	for neighbour in adj[cur]:
		if neighbour not in visited:
			if dfs(visited, adj, cur, neighbour):
				return True
		elif neighbour != parent:
			return True

	return False



def isCycleDetected(adj, vertexCount):
	visited = set()
	for cur in range(vertexCount):
		if cur not in visited and dfs(visited, adj, -1, cur):
			return True

	return False



vertexCount, edgeCount = map(int, input().split())
edges = readGraph(edgeCount)
adj = createAdjList(edges)
print(isCycleDetected(adj, vertexCount))
