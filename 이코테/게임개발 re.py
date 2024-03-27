# A , B  = 행( 세로 ) , 열 ( 가로 )
# N , M 입력 : 행 , 열

N, M = map(int, input().split())
directions = [0, 1, 2, 3]  # 인덱스 매핑 북, 동, 남, 서
dx = [-1,0,+1,0 ] # 행 ( 세로 )
dy = [0,+1,0,-1 ] # 열 ( 가로 )

x, y, direction = map(int, input().split())

d = [[0] * M for _ in range(N)]  # 방문장소 저장

array = []

for _ in range(N):
    array.append(list(map(int, input().split())))


def turn_left():
    global direction
    direction -= 1
    if (direction == -1):
        direction = 3


cnt =1
d[x][y] = 1
turntime =0;


while (True):
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny]==0 and array[nx][ny]==0:
        x , y = nx , ny

        d[x][y] = 1
        cnt+=1
        turntime=0

    else:
        turntime+=1

    if(turntime==4):
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny]==1:
            break
        else:
            x , y = nx , ny
            turntime = 0

print(cnt)

