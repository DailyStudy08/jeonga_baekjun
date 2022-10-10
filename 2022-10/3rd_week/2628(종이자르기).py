import sys
sys.stdin = open('input.txt', 'r')

C, R= map(int, input().split())
r, c = [0,R], [0,C]
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    if a == 0:
        r.append(b)
    elif a == 1:
        c. append(b)
r.sort()
c.sort()
x =[]; y =[]
for i in range(len(r)-1):
    x.append(r[i+1]-r[i])
for j in range(len(c)-1):
    y.append(c[j+1]-c[j])
maxV = 0
for i in range(len(x)):
    for j in range(len(y)):
        temp = x[i]*y[j]
        if temp > maxV:
            maxV = temp
print(maxV)
