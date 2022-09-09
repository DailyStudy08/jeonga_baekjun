N, K = map(int, input().split())
l =N - K
a = list(map(int,input().split(',')))
n = N
while K>0:
    for i in range(n-1):
        a[i] = a[i+1]-a[i]
    K -= 1
    n -= 1

b = list(map(str,a[:N-K]))
print(','.join(b))