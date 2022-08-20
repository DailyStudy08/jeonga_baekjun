def finder(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        else:
            return True

num_lst=[]
while True:
    n  = int(input())
    if n == 0:
        break
    else:
        num_lst.append(n)
# num_lst 완성

for n in num_lst:
    prime_lst = []
    for num in range(n+1, 2*n+1):
        if finder(num):
            prime_lst.append(num)
    # prime_lst 완성
    print(len(prime_lst))