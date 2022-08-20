M = int(input())
N = int(input())

prime_lst = []
for num in range(M, N+1):
    if num > 1:                     # 자연수로 만들어주는 것이 핵심 ...!
        for j in range(2, num):
            if num%j == 0:
                break
        else:
            prime_lst.append(num)

if not(prime_lst):
    print(-1)
else:
    print(sum(prime_lst))
    print(min(prime_lst))
