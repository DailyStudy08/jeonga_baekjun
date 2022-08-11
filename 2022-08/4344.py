T = int(input())
for _ in range(T):
    lstV = list(map(int,input().split()))
    N = lstV[0]
    lstV = lstV[1:]
    avgV = sum(lstV)/N
    cnt = 0
    for el in lstV:
        if el > avgV:
            cnt += 1
    print(f'{round(100*cnt/N,3):.3f}%')

    # f-string 의 출력양식을 정하기 가능