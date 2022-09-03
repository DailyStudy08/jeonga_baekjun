T = int(input())
for tc in range(T):
    H, W, N = map(int, input().split())
    n = N -1
    a = n % H
    b = n // H


    if b<9:
        print(str(a+1)+'0'+str(b+1))
    else:
        print(str(a+1)+str(b+1))