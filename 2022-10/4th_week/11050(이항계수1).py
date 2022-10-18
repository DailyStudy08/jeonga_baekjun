def factorial(n):
    result = 1
    for i in range(2,n+1):
        result = result*i
    return result

N, K = map(int, input().split())
a = 1
for i in range(K):
    a *= (N-i)

print(int(a//factorial(K)))
