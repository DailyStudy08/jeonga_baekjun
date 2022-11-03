import sys
sys.stdin = open('input.txt', 'r')


N, K = map(int, input().split())
check = [0] * (N+1)
numbers = []
for i in range(2, N + 1):
    for j in range(i, N + 1, i):
        if check[j]==0:
            check[j] = 1
            numbers.append(j)
            if len(numbers)>= K:
                break
print(numbers[K-1])