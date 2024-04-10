from collections import deque
N = int(input())
arr=[]
now_x, now_y=0,0

for i in range(N):
    arr.append(list(map(int,input().split())))
    for j in range(N):
        if arr[i][j]==9:
            now_x=i
            now_y=j
            arr[i][j]=0

dx=[-1,+1,0,0]#상하좌우
dy=[0,0,-1,+1]

now_size=2

def bfs():
    # 이동한 매 순간순간 현재 물고기들의 최솟값 배열을 반환하는 함수
    dist=[[-1]* N for i in range(N)]
    q=deque()

    q.append((now_x,now_y))
    dist[now_x][now_y]=0

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<N :
                # 주의 ! bfs는 반복문에서 x ,y 가 계속 사용되므로 swap 하면 안됨
                if dist[nx][ny]==-1 and arr[nx][ny]<=now_size :
                   dist[nx][ny]=dist[x][y]+1
                   q.append((nx,ny))
    return dist

def find(dist):
    # 거리가 가장 가까운 먹을수 있는 물고기의 위치와 거리를 구하는 함수
    minimum=1e9
    min_x,min_y=0,0
    # 0 , 0 부터 탐색하는 과정에서 자동으로 맨 왼쪽 맨 위 인덱스가 최솟값으로 저장됨
    for i in range(N):
        for j in range(N):
            if dist[i][j]!=-1 and 0<arr[i][j]<now_size:
                if dist[i][j]<minimum:
                    min_x, min_y=i,j
                    minimum=dist[i][j]

    if minimum==1e9:
        return None
    else:
        return minimum,min_x,min_y


time=0
eat_count=0
# 반복문 안에 두면 0으로 계속 재초기화됨.
while True:

    fish=find(bfs())
    if fish==None:

        break

    eat_count+=1
    time+=fish[0]

    now_x, now_y = fish[1], fish[2]
    # 먹은 위치에 아무것도 없도록 처리
    arr[now_x][now_y]=0

    if eat_count>=now_size:
        now_size+=1
        # 사이즈를 키운 다음에는 다시 사이즈 카운트를 0으로 초기화
        eat_count=0
print(time)




























