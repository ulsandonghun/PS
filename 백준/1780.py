import sys

num = int(sys.stdin.readline())
result = {-1: 0, 0: 0, 1: 0}

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(num)]


def recursive(row, cal, N):
    current = matrix[row][cal]
    for i in range(row,row+N):
        for j in range(cal,cal+N):
            checknum = matrix[i][j]
            if not isSame(checknum, current) :
                jump = N // 3
                recursive(row, cal, jump)
                recursive(row, cal + jump, jump)
                recursive(row, cal + jump * 2, jump)

                recursive(row + jump, cal, jump)
                recursive(row + jump, cal + jump, jump)
                recursive(row + jump, cal + jump * 2, jump)

                recursive(row + jump * 2, cal, jump)
                recursive(row + jump * 2, cal + jump, jump)
                recursive(row + jump * 2, cal + jump * 2, jump)
                return

    result[current] += 1
    return


def isSame(num, current):
    if num == current:
        return True
    else:
        return False

recursive(0,0,num)
for _ in result.values():
    print(_)
