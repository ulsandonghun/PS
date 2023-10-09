import sys

N =int(sys.stdin.readline())

lst=[]

for _ in range(N):
    a,b=map(int,sys.stdin.readline().strip().split())
    lst.append((a,b))
# lst.sort(key=lambda x : (x[0],x[1]) )  이 방법도 가능하고 파이썬은 어짜피순서대로 정렬하기 때문에 그대로 sort 만 써도 됨.
lst.sort()
for i in lst:
    print(i[0],i[1])

