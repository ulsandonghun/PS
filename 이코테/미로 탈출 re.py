# N , M 행(세로) , 열(가로)
from collections import deque

N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input())))

# BFS 의 이유 : 인접한 장소를 우선적으로 방문 -> 이전 값 +1 해주기

dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]
visited = [[False] * M for i in range(N)]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        popleft = queue.popleft()
        x = popleft[0]
        y = popleft[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M or arr[nx][ny] != 1:
                continue
            if  arr[nx][ny] ==1 : # 큐 안에 존재유무 대신, 해당 노드를 처음 방문하는 경우에만
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))



bfs(0, 0)

print(arr[N - 1][M - 1])
