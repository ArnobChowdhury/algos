def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)  # 0

    for next in graph[start] - visited:  # {1, 2}
        dfs(graph, next, visited)  # {next: 1}
    return visited


graph = {'0': set(['1', '2']),
         '1': set(['0', '3']),
         '2': set(['0', '4', '5']),
         '3': set(['1']),
         '4': set(['2', '6']),
         '5': set(['2']),
         '6': set(['4'])}

#[[1, 2], [0, 3], [0, 4, 5], [1], [2, 6], [2], [4]]
v = dfs(graph, '0')
print(v)

{'0', '5', '2', '3', '6', '1', '4'}
[0, 2, 5, 4, 6, 1, 3]
