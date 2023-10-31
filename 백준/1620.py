import sys

N , M =map(int,sys.stdin.readline().split())
dic=dict()
i=1
for _ in range(N):
    dic[sys.stdin.readline().strip()]=str(i)
    i+=1

# print(dic)
for j in range(M):
    word=sys.stdin.readline().strip()
    if(word in dic):
        print(dic[word])
    else:
        for key, value in dic.items():
            if(value==word):
                print(key)


