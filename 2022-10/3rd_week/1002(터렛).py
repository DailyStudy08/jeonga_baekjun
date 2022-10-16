import math

N = int(input())
for _ in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.pow(x1-x2,2) + math.pow(y1-y2,2)
    if d==0 and r1==r2:
        print(-1)
    elif d==math.pow(r1+r2,2) or d==math.pow(r1-r2,2):
        print(1)
    elif math.pow(r1-r2, 2)< d < math.pow(r1+r2,2):
        print(2)
    else:
        print(0)