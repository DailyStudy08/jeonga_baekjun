N= int(input())
# n번째 쉘
n=0
while 3*(n-1)*(n) + 1 < N:
    if 3*(n)*(n+1)+1 >= N:
        res = n
        break
    else:
        n += 1
print(n+1)
    
    