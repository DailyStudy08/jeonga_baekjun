# import sys
# sys.stdin = open('input.txt', 'r')

N = int(input())
a = list(map(int, input().split()))
p = [0]*N
idx = 0

while True:

    if idx == N:
        break
    min_idx = 0
    for i in range(N):
        if a[min_idx] > a[i]:
            min_idx = i
    p[min_idx]= idx
    a[min_idx] = 1000
    idx += 1
for i in range(N):
    print(p[i], end=' ')
