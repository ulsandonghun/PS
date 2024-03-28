# N 세로(행), M 가로(열)

# ( A , B ) x , y 행 , 열  0부터 시작
N, M = map(int, input().split())
x, y, direction = map(int, input().split())

directions = [0, 1, 2, 3]  # 북 동 남 서
dx = [-1, 0, +1, 0]
dy = [0, +1, 0, -1]

array = []

visited = [[0] * M for i in range(N)]

for _ in range(N):
    array.append(list(map(int, input().split())))


def turn_left():
    global direction
    direction -= 1
    if (direction == -1):
        direction = 3


visited[x][y] = 1
turn_time = 0
cnt = 1
while (True):
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if (visited[nx][ny] == 0 and array[nx][ny] == 0):
        x, y = nx, ny
        turn_time = 0
        cnt += 1
        visited[x][y]=1

    else:

        turn_time += 1
        if (turn_time == 4):
            nx = x - dx[direction]
            ny = y - dy[direction]

            if (array[nx][ny] == 1):
                break
            x, y = nx, ny
            turn_time=0
print(cnt)