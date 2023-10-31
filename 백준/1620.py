import sys

N , M =map(int,sys.stdin.readline().split())
dic_str_key=dict()
dic_int_key=dict()

i=1
for _ in range(N):
    input=sys.stdin.readline().strip()

    dic_str_key[input]=str(_+1)
    dic_int_key[str(_+1)]=input

for j in range(M):
    word=sys.stdin.readline().strip()
    if(word in dic_str_key):
        print(dic_str_key[word])
    else:
        print(dic_int_key[word])


