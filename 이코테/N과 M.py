N , M = map(int,(input().split()))

visited=[False] * (N+1)

list=[]

def dfs(cnt):
    if(cnt==M):
        print(" ".join(map(str,list)))
        return
    for i in range(1,N+1):

        if visited[i]:
            continue
        visited[i]=True
        list.append(i)
        dfs(cnt+1)
        visited[i]=False
        list.pop()

dfs(0)





