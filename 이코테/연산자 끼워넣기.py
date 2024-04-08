# dfs 백트레킹 or permutaion

N = int(input())

nums=list(map(int,input().split()))


add, sub , mul, div = map(int,input().split())

minimum=1e9
maximum=-1e9

def dfs(i, now):
    global add, sub, mul, div, N, minimum,maximum
    if i ==N:
        minimum = min(minimum, now)
        maximum = max(maximum, now)
        return

    else:
        if add>0:
           add-=1
           dfs(i+1,now+nums[i])
           add+=1
        if sub >0:
           sub-=1
           dfs(i+1,now-nums[i])
           sub+=1
        if mul>0:
            mul-=1
            dfs(i+1,now*nums[i])
            mul+=1
        if div>0:
            div-=1
            dfs(i+1,int(now/nums[i]))
            div+=1



dfs(1,nums[0])
print(maximum)
print(minimum)





