X = int(input())
cnt=0
dp=[0]*(X+1)
dp[1]=0
dp[2]=1

for i in range(3,X+1):
    dp[i]=min(dp[i-1]+1,dp[i//3]+1,dp[i//2]+1)

print(dp[X])

