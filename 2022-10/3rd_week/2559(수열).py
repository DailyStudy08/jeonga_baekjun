import sys
sys.stdin = open('input.txt', 'r')

import sys
N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

temp = 0
for i in range(M):
    temp += a[i]
maxV = temp

for j in range(N-M):
    temp = temp -a[j] + a[j+M]
    if temp>maxV:
        maxV = temp
print(maxV)


