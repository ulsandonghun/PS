# N N 으로 하고 1부터 시작 -> N+1 형태로 배열 생성

N = int(input())
data = [[0] * (N + 1) for i in range(N + 1)]

K = int(input())
for i in range(K):
    x, y = map(int, input().split())

    data[x][y] = 1

L = int(input())

info = []
for i in range(L):
    time, d = input().split()

    info.append((int(time), d))

dx = [0, +1, 0, -1]  # 동쪽에서 시작하므로 동 남 서 북
dy = [+1, 0, -1, 0]


def turn(direction, c):
    # print(c)

    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

    return direction





def Simulation():
    x, y = 1, 1
    data[x][y] = 2
    direction = 0
    time = 0
    index=0
    snack=[(x, y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if nx >= 1 and ny >= 1 and nx <= N and ny <= N and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                # 전진하는 위치 저장
                snack.append((nx, ny))
                data[nx][ny] = 2
                # 사과가 없을경우 기존 값 삭제후 전진
                i,j = snack.pop(0)
                data[i][j] = 0
        # 만약 사과가 존재하는 경우 삭제하지않고 뱀의 길이만 늘림.
            if data[nx][ny]==1:
                data[nx][ny]=2
                snack.append((nx,ny))
        else:
            time+=1
            break
        x,y =nx,ny
        time+=1
        if index<L and time==info[index][0]:
            # print(L)
            # print(index)
            ## 매우 중요 ! 한참 해맴, index를 더하는 위치 중요. index out of bound 애러
            direction = turn(direction, info[index][1])
            index+=1

    return time


print(Simulation())