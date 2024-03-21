r ,g, b=map(int,input().split())
sum=0
for i in range(r):
    for j in range(g):
        for k in range(b):
            sum+=1
            print(i,j,k)

print(sum)