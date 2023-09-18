N=int(input())
lst=map(int,input().split())
cnt=0

for i in lst :
    for j in range(2,i+1):
        # print("i의 값",i)
        if i%j==0 and i!=1:
            if(j!=i):
                break
            else:
                cnt+=1

print(cnt)





