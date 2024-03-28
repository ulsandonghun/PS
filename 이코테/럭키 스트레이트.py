N = input()

size = len(N)
Lsum=0
for i in range(size//2):
    Lsum+=int(N[i])
Rsum=0
for i in range(size//2,size):
    Rsum+=int(N[i])

if(Lsum==Rsum):
    print('LUCKY')
else:
    print('READY')