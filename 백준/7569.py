import sys
from collections import deque

M,N,H= map(int, sys.stdin.readline().split())

#M 개의 요소(열 : 가로) 를 읽어서 split()을 한 다음에 리스트로 만든다
#위의 과정을 N번 수행한다(행 : 세로)
matrix=[[list(map(int,sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

#방문한 곳을 기록하는 3차원 배열 : 여기서도 M번 False를 기록하기를 N번 반복
visited=[[[False]*M for _ in range(N)]for _ in range(H)]

queue = deque()

dx = [-1,1,0,0,0,0]#높이
dy = [0,0,-1,1,0,0]#세로
dz = [0,0,0,0,-1,1]#가로

answer= 0

def bfs():
    while queue:
        x,y,z = queue.popleft()

        for i in range(6):
            nx = x+dx[i]
            ny=y+dy[i]
            nz= z+dz[i]

            if nx<0 or nx>=H or ny<0 or ny>N or nz< 0 or nz>=M:
                continue
                #순서대로 높이/행(세로)/(가로) 순서의 좌표
            if matrix[nx][ny][nz] ==0 and visited[nx][ny][nz] ==False:
                queue.append((nx,ny,nz))
                matrix[nx][ny][nz] = matrix[x][y][z]+1
                visited[nx][ny][nz]=True

for a in range(H):
    for b in range(N):
        for c in range(M):
            if matrix[a][b][c]==1 and visited[a][b][c]==0:
                queue.append((a,b,c))
                visited[a][b][c]=True

bfs()



for a in matrix:
    for  b in a:
        for c in b:
            if c==0:
                print(-1)
                exit(0)
        answer=max(answer,max(b))
print(answer-1)



