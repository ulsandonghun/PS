# N * M : 행(세로) , 열(가로) 순으로 입력
#(A,B) A(세로 : 행) , B(가로 : 열)
N , M = map(int,input().split())
x, y , direction =map(int, input().split())

# 리스트 컴프리핸션으로 2차원배열 입력 받기
# array = [list(map(int,input().split())) for i in range(N)]
# 좀더 직관적인 입력 솔루션
array=list()

for i in range(N):
    array.append(list(map(int,input().split())))

# 방문 위치 저장

d=[[0]*M for i in range(N)]
# 현재위치 방문처리
d[x][y] =1

directionarr = [0,1,2,3] # 북, 동, 남, 서 #  각각의 인덱스의 위치 d[0],dx[0],dy[0] 이 북쪽방향 과 매핑
dx=[-1,0,+1,0]#행(세로)
dy=[0,+1,0,-1]#열(가로)

def turn_left():
    global  direction
    direction-=1
    if(direction ==-1):
        direction=3

count=0
turntime=0
while(True):
    turn_left()
    nx= x+dx[direction]
    ny= y + dy[direction]
    if d[nx][ny]==0 and array[nx][ny]==0:
        #이동이 수행될 경우
        x , y =nx, ny
        d[x][y]=1
        turntime=0
        count+=1
        continue
    else:
        turntime+=1
    if(turntime==4):
        break

print(count)






