S = input()

strarr=[]
sum=0

for i in range(len(S)):
    string=S[i]
    if string.isalpha() :
        strarr.append(string)
    else:
        sum+=int(string)

strarr.sort()
strarr.append(str(sum))


print("".join(strarr))

