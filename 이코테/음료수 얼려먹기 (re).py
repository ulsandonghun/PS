N, M = map(int, input().split())  # 세로(행 ) 가로 ( 열 )

arr = []
for _ in range(N):
    arr.append(list(map(int, input())))


def dfs(x, y):
    if(x<0 or y < 0 or x>=N or y >=M):

        return False
    if(arr[x][y]==1):
        return False

    arr[x][y]=1

    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)

    return True




count = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            count += 1

print(count)
