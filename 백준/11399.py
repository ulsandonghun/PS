import sys

N= int(sys.stdin.readline())
p=[]

p=list(map(int,input().split()))
p.sort()
result=0
#한번의 사이클마다 더해가는 수를 하나씩 늘려가야 함--> 이중for문
for i in range(len(p)):
    for j in range(0,i+1):
        result+=p[j]
print(result)







