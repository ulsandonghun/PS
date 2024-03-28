# N ,: 세로 (행)  M  : 가로 ( 열) , (1부터 시작, ) 현재위치 ( 1 ,1)
# 중요 !! 시뮬레이션이나 그래프 탐색은 모두 이동을 배열로 나뉘자 무조건
# BFS 는 가장 가까운 거리부터 방문하니 이전 노드의 값 +1을 하면 된다.
from collections import deque

N, M = map(int, input().split())

array = []

for _ in range(N):
    array.append(list(map(int, input())))  # 주의 공백 없이 입력받으므로, split 하지않고 입력

check = [[0] * M for i in range(N)]

dx = [-1, +1, 0, 0]  # 행( 세로) 상 하 좌 우
dy = [0, 0, -1, +1]  # 열 ( 가로 )

x, y = 0, 0
check[x][y] = 1


def bfs(i, j):
    global check
    global array
    queue = deque()
    queue.append((i, j))

    while queue:
        popleft = queue.popleft()
        x = popleft[0]
        y = popleft[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M or array[nx][ny] == 0 or check[nx][ny] == 1:

                continue
            array[nx][ny] = array[x][y] + 1
            # x, y = nx, ny 현재위치를 변경할 필요가 없음.

            check[nx][ny] = 1
            queue.append((nx, ny))


bfs(0, 0)

print(array[N - 1][M - 1])

