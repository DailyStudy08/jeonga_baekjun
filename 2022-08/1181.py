import sys
N = int(sys.stdin.readline())
mylst = [sys.stdin.readline().strip() for i in range(N)]

a = []
for i in range(N):
    a.append((len(mylst[i]), mylst[i]))
a.sort()
b=[]
for i in a:
    if i not in b: 
        b.append(i)
c=[]
for i in range(len(b)):
    c.append(b[i][1])
print('\n'.join(c)) 