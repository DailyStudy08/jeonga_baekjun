N, M = map(int, input().split())
a = list(map(int, input().split()))

result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            v1 = a[i] + a[j] + a[k]
            if v1 > M:
                continue
            else:
                if v1 > result:
                    result = v1
print(result)


