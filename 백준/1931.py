import sys
zero=[1,0,1]
one=[0,1,1]

def fibo(num):
    result_zero=0
    result_one=0
    if num>2:
        for i in range(3,num+1):
            result_zero=zero[i-1]+zero[i-2]
            print("zero",zero[i-1],"과 ",zero[i-2], "추가 ")
            result_one=one[i-1]+one[i-2]
            print("one",one[i-1],"과 ",one[i-2], "추가 ")
            zero.append(result_zero)
            one.append(result_one)

    return zero[num],one[num]

N = int(sys.stdin.readline())


for i in range(N):
    print(fibo(int(sys.stdin.readline())))
