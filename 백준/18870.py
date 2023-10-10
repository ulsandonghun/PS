import sys

N= int(sys.stdin.readline())

lst=[]
result=[]


lst=list(map(int,sys.stdin.readline().split()))

result=sorted(list(set(lst)))

dic={}
for i in range(len(result)):
    dic[result[i]]=i #어렵게 생각하지 말고, 리스트에 저장된 것을 그대로 딕셔너리로 옮긴 것임.
    #딕셔너리는 검색속도가 log 1 이기 때문임.

for i in lst:
    print(dic[i],end=" ") #dictionary를 이용해 검색 속도를 log(1)로 낮춤.
    # list의 index 검색은 log(N)임.


# for i in lst:
#     print(result.index(i),end=" ")