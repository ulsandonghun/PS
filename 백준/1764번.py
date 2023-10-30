import sys

N, M =map(int,sys.stdin.readline().split())

result=[]

setOfSee=set()
setOfHear=set()

for _ in range(N):
    setOfSee.add(input())
for _ in range(M):
    setOfHear.add(input())

intersection = setOfSee.intersection(setOfHear)
result = list(intersection)
result.sort()
print(len(result))
print("\n".join(str(i) for i in result))

