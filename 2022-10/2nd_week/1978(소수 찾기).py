def finder(num):
    if num==1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

N = int(input())
a =list(map(int, input().split()))
cnt = 0
for i in range(N):
    if finder(a[i]):
        cnt += 1
print(cnt)