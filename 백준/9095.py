T= int(input())

# 점화식 : f(n) = f(n-3)+f(n-2)+f(n-1)


for i in range(T):
    n = int(input())

    arr=[0]*(n+3+1)
    arr[1]=1
    arr[2]=2
    arr[3]=4

    for i in range(4,n+1):
        arr[i]=arr[i-3]+arr[i-2]+arr[i-1]

    print(arr[n])




