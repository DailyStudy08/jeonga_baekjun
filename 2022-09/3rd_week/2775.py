T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    floor = 0
    zero_floor = [0]*(n+1)
    for i in range(n+1):
        zero_floor[i] = i
    while True:
        if floor == k:
            break
        next_floor = [0]*(n+1)
        for i in range(n+1):
            for j in range(i+1):
                next_floor[i] += zero_floor[j]
        floor += 1
        zero_floor = next_floor
    print(next_floor[-1])


'''solution2'''
T = int(input())

for _ in range(T):
    floor = int(input())
    num = int(input())
    f = [x for x in range(1, num+1)]
    for k in range(floor):
        for i in range(1, num):
            f[i] += f[i-1]
            # 여기 잘 못하는 부분
    print(f[-1])