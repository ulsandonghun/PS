from collections import deque


def bfs(v):
    global visited
    global graph
    queue=deque()
    queue.append(v)
    while queue:
        print("현재 큐 상태")
        print(queue)
        popleft= queue.popleft()
        print(popleft,"출력")
        visited[popleft]=1
        print(popleft)
        for i in graph[popleft]:
            print("%d 의 방문검사 "%(i))
            if visited[i]==1 or i in queue:
                # 애러 원인 만약 방문 검사만 실행할시, 방문이 되지 않았지만 큐에는 대기중인 노드가 유효성 검사에서 빠짐.
                continue
            queue.append(i)
            print("%d 를 큐에 삽입"%i )


visited=[0] * 9

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
bfs(1)