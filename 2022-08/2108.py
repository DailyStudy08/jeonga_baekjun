N = int(input())
lst = [0] * N
for i in range(N):
    lst[i] = int(input())
# 1 산술평균
print(round(sum(lst)/N))
# 2 중앙값
lst.sort()

print(lst[N//2])
# 3 최빈값
cnt =[0]*8000
for i in range(len(lst)):
    cnt[lst[i]] += 1

idx=[]
for i in range(len(cnt)):
    if i <=4000:
        if cnt[i]==max(cnt):
            idx.append(i)
    else:
        if cnt[i]==max(cnt):
            idx.append(i-8000)

if len(idx) !=1:
    idx.sort()

    print(idx[1])
else:
    print(idx[0])

# 4 범위
print(lst[-1]-lst[0])

# 시간초과가 나네요....눈물이 납니다.
