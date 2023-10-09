import sys

N =int(sys.stdin.readline())

lst=[]

for _ in range(N):
    a,b=map(int,sys.stdin.readline().strip().split())
    lst.append((a,b))
lst.sort(key=lambda x : (x[0],x[1]) )

for i in lst:
    print(i[0],i[1])

