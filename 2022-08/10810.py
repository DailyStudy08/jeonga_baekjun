N, M = map(int, input().split())
basket = [-1] + [0]*N

for i in range(M):
    s, e, num = map(int, input().split())
    for j in range(s, e+1):
        basket[j] = num
# basket 완료

for i in range(1, N+1):
    print(basket[i], end=' ')