input=input()

row=ord(input[0])-ord('a')+1 # 열(가로)
colum=int(input[1]) # 행(세로)

# print(row,colum)

steps=[(-2,+1),(-2,-1),(+2,+1),(+2,-1),(-1,+2),(+1,+2),(-1,-2),(+1,-2)]
cnt=0

for step in steps:
    next_row= row + step[0]
    next_colum= colum + step[1]
    if next_row>=1 and next_row<=8 and next_colum>=1 and next_colum<=8:
        cnt+=1

print(cnt)
