N = int(input())
orders = list(input().split())

x , y= 1 , 1 # 현재위치
dx = [0,0,-1,+1]# 행(세로) (dx, dy)
dy = [-1,+1,0,0]# 열(가로)
move_plans = ['L','R','U','D']

for order in orders:
    for i in range(len(move_plans)):
        if(order == move_plans[i]):
            nx = x + dx[i]
            ny = y + dy[i]

    if(nx <1 or ny < 1 or nx>N or ny > N):
        continue

    x , y = nx , ny




print(x,y)
