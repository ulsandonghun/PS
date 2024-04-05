# N * N 행 (세로) 열 ( 가로 )
N = int(input())

arr = [[0] * (N + 1) for i in range(N + 1)]

K = int(input())
for i in range(K):
    x, y = map(int, input().split())
    arr[x][y] = 1

L = int(input())
info = []

for i in range(L):
    time, order = input().split()
    info.append((int(time), order))

dx = [0, +1, 0, -1]  # (행) 동 남 서 북
dy = [+1, 0, -1, 0]  # 열

x, y = 1, 1
arr[x][y] = 2
direction=0

def turn_direction(c):
    global direction
    if(c=='L'):
        direction=(direction-1)%4
    else:
        direction=(direction+1)%4

def Simulation():
    time = 0
    index=0
    global x , y, direction

    snack=[]
    snack.append((1,1))

    while True:
        nx = x + dx[direction]
        ny= y + dy[direction]

        if 1<=nx and nx<=N and 1<=ny and ny<=N and arr[nx][ny]!=2:
            if arr[nx][ny] ==1:
                snack.append((nx,ny))
                arr[nx][ny]=2
                time+=1
            else:
                # 만약 사과가 아닐 시에 기존 큐의 값을 빼주고 2 해제한다.
                pop = snack.pop(0)
                arr[pop[0]][pop[1]]=0

                snack.append((nx,ny))
                arr[nx][ny]=2
                time+=1
        else:
            time+=1
            break
        x , y = nx , ny

        if index<L and time==info[index][0]:
            turn_direction(info[index][1])
            index+=1

    return time

print(Simulation())







