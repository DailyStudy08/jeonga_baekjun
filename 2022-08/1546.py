N = int(input())
a = list(map(int, input().split()))
maxV = -1
for el in a:
    if el > maxV:
        maxV = el
sumV = 0
for el in a:
    sumV += el
print(sumV*100/(maxV*N))
