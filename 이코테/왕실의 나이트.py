#x, y 순서 , 행(세로), 열(가로)

input=input()

x = int(input[1])
y = input[0]

x =int(x) # 행 은 1 ,2,3,4~
y = ord(y) -int(ord('a'))+1 # 열 은 a,b,c ~
# 주의 아스키 코드로 변환 함수 = ord


dx=[-1,+1,-1,+1,-2,-2,+2,+2]#행(세로)
dy=[-2,-2,+2,+2,-1,+1,-1,+1]#열(가로)
move_plan=["LU","LD","RU","RD","UL","UR","DL","DR"]

cnt =0

for i in range(len(move_plan)):
    nx = dx[i] + x
    ny = dy[i] + y

    if(nx<1 or ny < 1 or nx>8 or ny > 8):
        continue
    cnt+=1

print(cnt)