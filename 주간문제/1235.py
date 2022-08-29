N =int(input())
mylst = [0]*N
for i in range(N):
    a = input()
    mylst[i] =a[::-1]
num=[0]*N
idx= 0
while True:
    for i in range(N):
        num[i] = mylst[i][0:idx+1]
    if len(set(num)) == N:
        break
    else:
        idx += 1
print(idx+1)


