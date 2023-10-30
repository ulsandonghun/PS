import sys

N = int(sys.stdin.readline())
dict={}
list_nums=list(map(int,sys.stdin.readline().split()))

for num in list_nums:
    if num not in dict:
        dict[num]=1
    elif num in dict:
        dict[num]+=1

list_nums.clear()
M=int(sys.stdin.readline())
list_nums=list(map(int,sys.stdin.readline().split()))

print(" ".join(str(dict[i]) for i in list_nums if i in dict))





