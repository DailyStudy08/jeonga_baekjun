N, K = map(int, input().split())
sumV=0
for i in range(K+1):
    sumV += 2**i
if sumV >=N:
    print('yes')
else:
    print('no')