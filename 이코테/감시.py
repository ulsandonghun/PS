import copy

n , m = map(int,input().split())

cctv=[]
graph=[]
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

dx = [-1,0,+1,0] # 북 동 남 서
dy=[0,+1,0,-1]

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(m):
        if graph[i][j] in [1,2,3,4,5]:
            cctv.append([graph[i][j],i,j])

def fill(board,direction,x,y):
    # cctv의 방향
    for i in direction:
        # cctv의 초기 위치
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                break
            if board[nx][ny]==6:
                break
            elif board[nx][ny]==0:
                board[nx][ny]=7
def dfs(depth,arr):
    global minimum

    if depth == len(cctv):
        count=0
        for i in range(n):
            count+=arr[i].count(0)
        minimum=min(minimum,count)
        return
    temp = copy.deepcopy(arr)
    cctv_num, x,y = cctv[depth]
    for i in mode[cctv_num]:
        # dfs 탐색 전 cctv 위치 채우기
        fill(temp,i,x,y)
        dfs(depth+1,temp)
        temp = copy.deepcopy(arr)
        # dfs 탐색 후 cctv 위치 초기화

minimum=1e9
dfs(0,graph)
print(minimum)
