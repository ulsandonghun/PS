# 조합 + dfs
import copy

N, M = map(int, input().split())

arr = []
virus = []
wall = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(M):
        c = arr[i][j]
        if c == 2:
            virus.append((i, j))
        if c == 0:
            wall.append((i, j))


def combination(arr, n):
    result = []
    if n == 0:
        return
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:

        for i in range(len(arr) - n + 1):
            for j in combination(arr[i + 1:], n - 1):
                result.append([arr[i]] + j)
    return result


candidates = combination(wall, 3)


# print(candidates)

dx = [-1,+1,0,0 ] #상 하 좌 우
dy = [0,0,-1,+1 ]



def dfs(x, y, arr):

    for i in range(4):
       nx = x + dx[i]
       ny = y + dy[i]

       if nx >=0 and ny >= 0 and nx<N and ny<M:

           if arr[nx][ny]!=0:
               continue

           arr[nx][ny]=2
           dfs(nx,ny,arr)

    return


def get_score(arr):
    result = 0
    for i in range(N):
        for j in range(M):
            if (arr[i][j] == 0):
                result += 1
    return result


def make_wall(comb):
    tmp_arr = copy.deepcopy(arr)
    for x, y in comb:
        tmp_arr[x][y] = 1

    for x, y in virus:
        dfs(x, y, tmp_arr)


    return get_score(tmp_arr)


result = 0 # 최종 값은 반복문 밖에 존재해야함
for comb in candidates: # 각 벽을 세웠을때 마다 가장 많은 안전영역을 차지한 곳으로 변경
    # comb = [[1,2],[2,3],[3,4]]
    wall2 = make_wall(comb)

    result = max(result, wall2)

print(result)
