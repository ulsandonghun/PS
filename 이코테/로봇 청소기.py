from collections import deque

N , M = map(int,input().split())
r, c, direction = map(int, input().split())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))


dx=[-1,0,+1,0] # 상 우 하 좌
dy=[0,+1,0,-1]


def turn_left():
    global direction
    direction=(direction-1)%4


def Simulation(init_X,init_Y):

    q=deque()
    q.append((init_X,init_Y))

    arr[init_X][init_Y]=2

    while q:
        x,y=q.popleft()
        count=0
        arr[x][y]=2

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M :
                if arr[nx][ny] == 0:

                    count+=1

        if count!=0:
            for i in range(4):
                turn_left()
                nx = x + dx[direction]
                ny = y + dy[direction]

                if 0 <= nx < N and 0 <= ny < M:
                    if arr[nx][ny] == 0:
                        q.append((nx,ny))
                        # 중요 ! 내가 실수한 부분 : 바로 전진 후 방문, 청소 하는 표현(1번으로 돌아가기)
                        break
        if count==0:
            nx = x - dx[direction]
            ny = y - dy[direction]
            if 0<=nx<N and 0<=ny<M :
                if arr[nx][ny] == 1:
                    break
                else:
                    q.append((nx,ny))


Simulation(r,c)
result=0
for i in range(N):
    for j in range(M):
        if arr[i][j]==2:
            result+=1

print(result)











