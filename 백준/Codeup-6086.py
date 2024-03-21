n = int(input())

i = 0
sum = 0
while (True):
    sum += i
    if (sum >= n):
        break

    i += 1
print(sum)
