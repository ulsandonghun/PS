import sys

N , K = map(int,sys.stdin.readline().split())
cnt=0;

result=[]
queue=[i for i in range(1,N+1)]

while(queue):
    cnt+=K-1
    #K-1 만큼 인덱스를 건너띄어서 큐에서 삭제
    if cnt>=len(queue):
        cnt%=len(queue)
    result.append(str(queue.pop(cnt)))
    #join을 써서 배열을 문자열로 바꾸기 위해 각 요소들을 문자 배열로 저장함.


print("<",", ".join(result),">",sep="")

