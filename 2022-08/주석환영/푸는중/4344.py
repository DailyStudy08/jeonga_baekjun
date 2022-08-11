C = int(input())

import sys
lstV = [] 
for i in range(C):
    mylst = list(map(int, sys.stdin.readline().split()))
    avgV = sum(mylst[1:])/mylst[0]
    cnt = 0
    for el in mylst[1:]:
        if el > avgV:
            cnt += 1 
    lstV.append(cnt/mylst[0] * 100)
for el in lstV:
    print(f'{round(el, 3)}%')