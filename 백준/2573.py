import sys
from collections import deque

#입력받을때, N: 행(세로), M: 열 (가로) [N][M]
N,M = map(int,sys.stdin.readline().split())

matrix=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]




def bfs(x,y):
    q= deque([(x, y)])
    visited[x][y]=1
    seaList=[] #녹임 대상이되는 좌표정보와 몇번 녹일지의 정보를 담는 리스트

    while q:
        x,y=q.popleft()
        sea=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if not matrix[nx][ny]:#주변 바다를 확인
                    sea+=1#바다 존재하면 해당 튜플의 sea+1함
                elif matrix[nx][ny] and not visited[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny] =1
        if sea>0:
            seaList.append((x,y,sea))
    for x,y,sea in seaList:
        #최종적으로 녹임의 대상이 되는 튜플들을 불러와서 녹인다.
        #단 0 이하로 녹이면 안되므로 max를 사용한다.
        matrix[x][y]=max(0,matrix[x][y]-sea)

    return 1

ice=[]
for i in range(N):
    for j in range(M):
        if matrix[i][j]:
            ice.append((i,j))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
year =0

while ice:
    visited=[[0]*M for _ in range(N)]
    deList=[]
    group = 0
    for i, j in ice:
        if matrix[i][j] and not visited[i][j]:
            group+=bfs(i,j)
        if matrix[i][j]==0:
            deList.append((i,j))
    if group > 1:
        print(year)
        break
    ice = sorted(list(set(ice)-set(deList)))
    year+=1
if group<2:
    print(0)








