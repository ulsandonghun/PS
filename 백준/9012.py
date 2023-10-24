import sys

T = int(sys.stdin.readline())
stack=[]

def  judge(str,stack=[]):

    arr=[ ]
    arr=list(str)
    for i in arr:
        if len(stack)>0:
            if(stack[-1]=='('and i==')'):
                stack.pop()
            elif( stack[-1]==')'and i==')'):

                stack.append(i)
                # print("break 수행 전현재 스택의 상태 : ",stack)
                break
            else:
                stack.append(i)
                # print("현재 스택의 상태 : ",stack)
        else:
            stack.append(i)

    if stack:
        # print("현재 스택의 상태 : ",stack)
        print("NO")
    else:
        # print("현재 스택의 상태 : ",stack)
        print("YES")
    stack.clear()

for _ in range(T):
    str=sys.stdin.readline().strip()
    judge(str,stack)
