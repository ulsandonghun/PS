# 2차원 배열 만들 필요 없음

dx=[-1,+1,-1,+1,-2,-2,+2,+2] # 행(세로) : 123456
dy=[-2,-2,+2,+2,-1,+1,-1,+1] # 열(가로) : a,b,c
move_plans=["LU","LD","RU","RD","UL","UR","DL","DR"]

input = input()

now_row = ord(input[0]) - ord('a') +1 # 열 ( dy )
now_column = int(input[1]) # 행 (dx)

cnt =0

for i in range(len(move_plans)):
    nx = now_column + dx[i]
    ny = now_row + dy[i]

    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    cnt+=1

print(cnt)

