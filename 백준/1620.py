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
    for key, value in dic.items():
        if(word == key):
            # print("현재"+word+"값이 key 값으로 존재함으로 value 값인 "+dic[word]+"값을 반환합니다.")
            print(dic[word])
        elif(word == value):
            # print("현재"+word+"값이 value 값으로 존재함으로 key 값인 "+key+"값을 반환합니다.")
            print(key)

