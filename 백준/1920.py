import sys

N = int(sys.stdin.readline())
lst = []

lst=list(map(int,sys.stdin.readline().split()))

dic={}
for i in range(len(lst)):
    dic[lst[i]]=i

M = int(sys.stdin.readline())

search=[]

search=list(map(int,sys.stdin.readline().split()))

for _ in search:
    if _ in dic:
        print(1)
    else:
        print(0)