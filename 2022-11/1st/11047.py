import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort(reverse=True)

result = 0
for el in arr:
    if K >= el:
        result += K//el
        K %= el
        if K <= 0:
            break
print(result)
