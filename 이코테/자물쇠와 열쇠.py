
def rotate_a_matrix_90_degree(a):
    column=len(a)
    row=len(a[0])
    result = [[0]*column for i in range(row)]

    for i in range(column):
        for j in range(row):
            result[j][column-i-1]=a[i][j]
    return result
def check(a):
    size = len(a)//3
    for i in range(size,size*2):
        for j in range(size, size*2):
            if a[i][j]!=1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock=[[0] * (3*n) for i in range(3*n)]

    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j]=lock[i][j]

    for i in range(4):
        rotate_a_matrix_90_degree(key)

        # lock 배열에서 키를 꽂을 시작 점을 잡아줌.
        for x in range(2 * n):
            for y in range(2* n):
                # lock 배열의 시작점으로부터 key 배열 값 전부를 하나하나 더함.
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]+=lock[i][j]
                if check(lock):

                    return True
                for  i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]-=lock[i][j]
    return False





key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
