import sys

N=int(sys.stdin.readline())
queue=[]
for _ in range(N):
    word=sys.stdin.readline().split()
    if(word[0]=="push"):
        queue.append(word[1])
    elif(word[0]=="pop"):
        if(len(queue)==0):
            print(-1)
        else:
            print(queue.pop(0))

    elif(word[0]=="size"):
        print(len(queue))

    elif(word[0]=="empty"):
        if(not queue):
            print(1)
        else:
            print(0)
    elif(word[0]=="front"):
        if(len(queue)==0):
            print(-1)
        else:
            print(queue[0])
    elif(word[0]=="back"):
        if(len(queue)==0):
            print(-1)
        else:
            print(queue[len(queue)-1])




