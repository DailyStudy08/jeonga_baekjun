N = int(input())
data =[[0]*(5) for _ in range(N)]
#
for i in range(N):
    data[i] = list(input().split())

cnt = [[] for _ in range(N)]
for i in range(5):
    for j in range(N-1):
        for idx in range(j+1, N):
            if data[j][i] == data[idx][i]:
                cnt[j].append(idx)
                cnt[idx].append(j)
max_idx= -1
maxV = -1
for i in range(N):
    if maxV<len(set(cnt[i])):
        maxV = len(set(cnt[i]))
        max_idx = i
print(max_idx+1)


'''
+ 데이터의 모습
+ 문제의 요구사항
'''

