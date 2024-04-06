from itertools import combinations

N , M = map(int, input().split())

arr= []

house=[]
chicken=[]

for i in range(N):
    arr.append(list(map(int,input().split())))
    for j in range(N):
        k=arr[i][j]
        if k==1:
            house.append((i,j))
        elif k==2:
            chicken.append((i,j))
def combination(arr,n):
    result=[]

    if n==0:
        return
    if n==1:
        for i in arr:
            result.append([i])
        return result
    elif n>1:
        for i in range(len(arr)-n+1):
            for j in combination(arr[i+1:],n-1):

                result.append([arr[i]]+j)

    return result

candidates=combination(chicken,M)
print(candidates)
# candidates=list(combinations(chicken,M))

def get_chickenlength(candidates):
    sum=0
    for x , y in house:
        temp=1e9
        # 조합으로 선별된 치킨집중  각 집들의 치킨거리를 구함.
        for c in candidates:
            print(c)
            print(c[0],c[1])
            temp= min(temp,abs(x-c[0])+abs(y-c[1]))
        sum+=temp
    return sum


temp=1e9 # 이것이 반복문 안에 있어서 오류가 났던 것임.
for comb in candidates:
    print(comb)
    temp=min(temp,get_chickenlength(comb))

print(temp)








