N , M = list(map(int, input().split()))


result=[]
def dfs(k):
    if len(result)==M:
        print(" ".join(map(str,result)))

        return

    for i in range(k,N+1):

        if i not in result:
            result.append(i)

            dfs(i + 1)

            result.pop()



dfs(1)


