import sys

N = int(sys.stdin.readline())
list=[]

for _ in range(N):
    x,y = map(int, sys.stdin.readline().split())
    list.append((x,y))

list.sort(key = lambda x: (x[0], x[1]))

for _ in list:
    print(_[0],_[1])
