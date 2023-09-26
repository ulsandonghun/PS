import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    word = sys.stdin.readline().strip()
    arr.append(word)
arr=list(set(arr))
arr.sort(key=lambda x : ( len(x),x))

for _ in arr:
    print(_)
