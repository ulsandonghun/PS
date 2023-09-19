import sys
N =int(sys.stdin.readline())
stack=[]

def push(x):
    stack.append(x)
def pop():
    if(len(stack)==0):
        print(-1)
    else:
        print(stack.pop())
def size():
    print(len(stack))
def empty():
    if(not stack):
        print(1)
    else:
        print(0)
def top():
    if (len(stack) == 0):
        print(-1)
    else:
        print(stack[-1])

for i in range(N):
    word=sys.stdin.readline().split()
    if(word[0]=="push"):
        x=word[1]
        # print("word[3]",word[2])
        # print("push 삽입:",x)
        push(x)
    elif(word[0]=="pop"):
        pop()
    elif(word[0]=="size"):
        size()
    elif(word[0]=="empty"):
        empty()
    elif(word[0]=="top"):
        top()


