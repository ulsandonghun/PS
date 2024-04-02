N = int(input())
K = int(input())

arr = [[0] * N for i in range(N)]
for i in range(K):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = 1

L = int(input())
direcion = 1
x, y = 1, 1

visited=[[False]*N for i in range(N)]
visited[0][0]=True

directions = [0, 1, 2, 3]  # 상 우 하 좌 인덱스 매핑
dx = [-1, 0, 0, +1]  # 상 우 하 좌
dy = [0, +1, -1, 0]  # 상 우 하 좌


def turn_left():
    global direction
    direction -= 1
    if (direction < 0):
        direction = 3


def turn_right():
    global direction
    direction += 1
    if (direction > 3):
        direction = 0


for i in range(L):
    time, d = input().split()
    time = int(time)
    # 3 D

    for j in range(time):
        nx = x + dx[direcion]
        ny = y + dy[direcion]
        if nx<=0 or ny<=0 or nx>=N or ny >=N:
            break
        if visited[nx][ny]==1:
            break
        if arr[nx][ny] ==1:
            visited[]


