N, M = map(int, input().split())
set_l = [0]*M
single_l = [0]*M
for i in range(M):
    set_l[i], single_l[i] = map(int, input().split())
# 가격
set_p = min(set_l)
single_p = min(single_l)

j = 0
while True:
    if 6*j<= N <6*(j+1):
        k = j
        break
    else:
        j += 1
# k 완성

result = 0
if set_p/6 <= single_p:
    result = set_p * k + single_p * (N - 6*k)
    if set_p < single_p * (N-k*6):
        result = set_p * (k+1)
else:
    result = single_p * N

print(result)