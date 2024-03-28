def dfs(v):
    global graph
    global visited
    if visited[v] == 1:
        return
    print(v)
    visited[v] =1
    for i in graph[v]:
        dfs(i)




# 노드가 총 9개
visited = [0] * 9

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
dfs(1)
