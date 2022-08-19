def fibo_dp(n):
    if n <3:
        return n
    else:
        a, b= b, a+b
        return b

n = int(input())
print(fibo_dp(n))