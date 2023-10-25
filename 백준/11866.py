import sys

N , K = map(int,sys.stdin.readline().split())
cnt=1;
queue =[]
result=[]
for _ in range(1,N+1):
    queue.append(_)

while(queue):
    first=queue[0]
    if(cnt%K==0):
        queue.remove(first)
        result.append(first)
    else:
        queue.remove(first)
        queue.append(first)
    cnt+=1
print("<",end="")
for _ in range(len(result)):
    if(_<len(result)-1):
        print(result[_],end="")
        print(", ",end="")
    else:
        print(result[_],end="")
print(">")
