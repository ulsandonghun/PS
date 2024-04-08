# bfs 를 이용한 탐색 -> 가능한 연합이면 bfs 추가
from collections import deque
import copy

N, L, R = map(int, input().split())

arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

dx = [-1, +1, 0, 0]  # 상하좌우
dy = [0, 0, -1, +1]  # 상 하 좌 우



def process(x, y, index):
    united = []
    united.append((x, y))

    q = deque()
    q.append((x, y))

    union[x][y] = index  # 방문 표시
    summary=arr[x][y]
    count=1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and union[nx][ny] == -1:

                if L <= abs(arr[nx][ny] - arr[x][y]) <= R :
                    # 실수주의 !! BFS 는 여기서 x,y 값을 바꾸면 안됨. 반복문이 계속 돌아가기 때문

                    q.append((nx, ny))
                    union[nx][ny]=index
                    united.append((nx, ny))
                    summary+=arr[nx][ny]
                    count+=1

    # sum = 0
    # mean = 0
    # for i, j in united:
    #     sum += arr[i][j]
    #     # 이러면 안되는 이유가 arr의 값이 변할 경우


    for i, j in united:
        arr[i][j] = summary // count

total_count=0

while True:
    union = [[-1] * N for i in range(N)]
    # 여기서 모든 값들을 -1로 처리해서 매 반복마다 국경개방이 전부 이루어 졌는지 확인.

    index=0
    for i in range(N):
        for j in range(N):
            if union[i][j] == -1:
                process(i, j, index)
                index+=1
    if index==N*N:
        break
    total_count +=1

print(total_count)


