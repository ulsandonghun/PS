N  = int(input())
h , m , s = 0 , 0 , 0
cnt=0
for h in range(0,N+1):
    # h+=1 오해 : 파이썬의 반복문은 해당 반복 끝나고 자동으로 변수 h 를 +1 해줌. 그래서 별도로 더해줄 필요가 없음.
    for m in range(0,60):
        # m+=1
        for s in range(0,60):
            # s+=1
            if '3' in str(h)+str(m)+str(s):
                cnt+=1

print(cnt)

