import sys

N = int(sys.stdin.readline())


lst =[]

for _ in range(N):
    a,b=sys.stdin.readline().strip().split()

    lst.append((int(a),b))
lst.sort(key = lambda x: x[0])

for _ in lst:
    print(_[0],_[1])

