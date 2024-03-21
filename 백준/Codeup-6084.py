w,h,b = map(int,input().split())


def method_name():
    return w * h * b / 8 / 1024 / 1024


res = method_name()
print('%.2f'%res,"MB")