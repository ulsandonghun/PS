from collections import deque
import copy

n , m = map(int,input().split())
arr= []
# cctv 저장 값 : 유형과 위치
cctv=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
    for j in range(m):
        if arr[i][j] in [1,2,3,4,5]:
            cctv.append([arr[i][j],i,j])

# 각 CCTV 유형별 감시회전 시야 분류 1번부터
mode = [
    [],
    [[0],[1],[2],[3]],
    [[1,3],[2,4]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,3],[0,1,2],[1,2,3],[2,3,0]],
    [[0,1,2,3]]
]
dx = [-1,0,+1,0] # 북 동 남 서
dy = [0,+1,0,-1]

# dfs 를 이용한 완전탐색으로 풀어야함.
def dfs(depth, arr):
    global minimum
    if depth==len(cctv): # 총 CCTV의 갯수만큼 깊어지면 되돌아감
        count=0
        for i in range(n):
            count+=arr[i].count(0)
            # count 메서드를 이용해서 해당 배열의 사각지대 갯수를 저장
        minimum=min(minimum,count)
        return

    temp=copy.deepcopy(arr)
    type,x,y=cctv[depth]

    for i in mode[type]:
        fill_sight(i,x,y,temp)
        dfs(depth+1,temp)
        temp=copy.deepcopy(arr)

def fill_sight(type,x,y,arr):
    nx , ny = x,y
    while True:
        nx +=dx[type]
        ny +=dy[type]
        if nx<0 or ny<0 or nx>=n or ny >=m:
            break
        if arr[nx][ny] ==6:
            break
        else:
            arr[nx][ny]=7

dfs(0,arr)








