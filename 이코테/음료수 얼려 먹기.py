# N 행 ( 세로 ) M 열 ( 가로 )

N, M = map(int, input().split())

array = []

for _ in range(N):
    array.append(list(map(int, input())))


def dfs(x, y):

    if x<0 or y <0 or x>=N or y>=M:
        return False

    if array[x][y] == 1:
        return False
    array[x][y]=1

    dfs(x-1,y) # 상
    dfs(x+1,y) # 하
    dfs(x,y-1) # 좌
    dfs(x,y+1) # 우

    return True



result = 0
for i in range(N):
    for j in range(M):

        if dfs(i, j):
            result += 1

print(result)
