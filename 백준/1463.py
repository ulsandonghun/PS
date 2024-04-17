X = int(input())
cnt=0

while(True):
    if (X == 1):
        break
    if((X%3)==0):
        X/=3
        cnt+=1
        print(X)
        continue
    if(X%2==0):
        X/=2
        cnt+=1
        print(X)
        continue
    X-=1
    cnt+=1
    print(X)

print(cnt)


