N, K = map(int, input().split())
sumV = 0

#  block
for i in range(K+1):
    sumV += 2**i
#  /block
if sumV >=N:
    print('yes')
else:
    print('no')
    
'----------using Bitwise Operators -------------'
# block
sumV = 0
for i in range(K+1):
    sumV += (1<<i)
# /block