N_s = int(input())
card = set(map(int, input().split()))
M = int(input())
check_num = list(map(int, input().split()))

for i in range(M):
    if check_num[i] in card:
        check_num[i] = 1
    else:
        check_num[i] = 0
print(*check_num)