vertexList = [0, 1, 2, 3, 4, 5, 6]
edgeList = [(0, 1), (0, 2), (1, 0), (1, 3), (2, 0), (2, 4),
            (2, 5), (3, 1), (4, 2), (4, 6), (5, 2), (6, 4)]
graphs = (vertexList, edgeList)


def bfs(graph, start):
    vertexList, edgeList = graph
    adjList = [[] for vertex in vertexList]
    visited = []
    queue = [start]

    for edge in edgeList:
        adjList[edge[0]].append(edge[1])

    print('adjList', adjList)

    while queue:
        current = queue.pop()
        for neighbor in adjList[current]:
            if not neighbor in visited:
                queue.insert(0, neighbor)
        visited.append(current)
    return visited


print(bfs(graphs, 0))
