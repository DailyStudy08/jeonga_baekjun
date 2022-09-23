import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b_1 = b[::]
max_idx_lst = []
while True:
    if len(max_idx_lst)==N:
        break
    maxV = -1
    max_idx = 0
    for i in range(N):
        if maxV < b[i]:
            maxV = b[i]
            max_idx = i
    if i == N-1:
        max_idx_lst.append(max_idx)
        b[max_idx] = -1
a.sort()
s = 0
for j in range(N):
    s += a[j]*b_1[max_idx_lst[j]]
print(s)
