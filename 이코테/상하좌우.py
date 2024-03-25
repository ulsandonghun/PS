N = int(input())
orders = list(map(str, input().split()))

# arr=[[0] * N for i in range(N) ] 필요가 없음. 현재위치를 좌표로만 저장하면 됬다.
x, y = 1, 1 # 주의 여기서 x, y 는  세로(행), 가로(열) 임, 요약 : x,y좌표 반대

# dx = [-1, +1, 0, 0]이것은 기존 x, y 좌표대로 한 것임 -> 이문제는 행, 열 기준으로 좌표를 해야함.
# dy = [0, 0, +1, -1]

dx = [0, 0, -1, +1] # 행(세로)
dy = [-1, +1, 0, 0] # 열(가로)
move_types = ['L', 'R', 'U', 'D']

for m in orders:
    for i in range(len(move_types)):
        if m == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > N or ny < 1 or ny > N:
        continue
    x,y=nx,ny


print(x,y)

## 주의 : 상식적인 Up down 을 생각하지 말고, 문제의 정의대로 구현하자