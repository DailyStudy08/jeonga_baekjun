N, K = map(int, input().split())
check=[[0]*7 for _ in range(2)]
for i in range(N):
    a, b = map(int, input().split())
    check[a][b] += 1
cnt = 0
for i in range(1,7):
    c1 = check[0][i]
    c2 = check[1][i]
    if c1%K==0:
        cnt += c1//K
    else:
        cnt += c1//K + 1
    if c2%K==0:
        cnt += c2//K
    else:
        cnt += c2//K + 1
print(cnt)

