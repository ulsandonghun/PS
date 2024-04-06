from itertools import combinations
# 1부터 시작
N , M  = map(int,input().split())

arr=[]
house=[]
chicken=[]

for i in range(N):
    arr.append(map(int,input().split()))
    for j in range(N):
        if arr[j]==1:
            house.append((i,j))

        elif arr[j]==2:
            chicken.append((i,j))

comb = combinations(chicken, M)

def get_sum_House(chickencomb):
    #각 조합마다 집 별
    temp =1e9
    for x,y in house:
        temp=min(temp,abs(x-chickencomb[0])+abs(y-chickencomb[1]))
    return temp




result=0
for c in comb:
    result+=get_sum_House(c)






