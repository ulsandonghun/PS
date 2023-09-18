while True:
    num=input()
    if(num=='0'):
        break
    stack=[]
    str=""
    for i in num:
        stack.append(i)

    for i in range(len(stack)):
        str+=stack.pop()
    if(str==num):
        print("yes")
    else:
        print("no")

