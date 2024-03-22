n = int(input())

arr=list(map(int,input().split()))
d=dict()


for _ in range(1,24):
    d[_]=0

for i in arr:
    d[i]+=1

for i in d.values():
    print(i,end=" ")

