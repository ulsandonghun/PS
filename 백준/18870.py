import sys

N= int(sys.stdin.readline())

lst=[]
result=[]

cnt=0
for _ in range(N):
    lst=list(map(int,sys.stdin.readline().split()))

lst.sort(key = lambda  x :x[0] )
for i in lst:
    print()