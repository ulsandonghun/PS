import sys

N = int(sys.stdin.readline())
lst=[]
for _ in range(N):
    lst.append(sys.stdin.readline().strip())

set= set(lst)
lst = list(set)
lst.sort(key=lambda x:(len(x),x))

for _ in lst:
    print(_)
