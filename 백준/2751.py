import sys

N = (int(sys.stdin.readline()))
arr= [ ]
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
arr=list(set(arr))
arr.sort(key = lambda x: x)

for _ in arr:
    print(_)
