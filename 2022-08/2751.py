import sys
N = int(sys.stdin.readline())
a = []
for _ in range(N):
    a.append(int(sys.stdin.readline()))
# 입력 받기
# 정렬 하기
for i in range(N-1):
    minIdx = i
    for j in range(i+1, N):
        if a[minIdx] > a[j]:
            minIdx = j
            a[i], a[minIdx] = a[minIdx], a[i]
for el in a:
    print(el)
    
    # 입력과 출력에서, 수가 관련되면 str인지 int인지 분명하게 데이터 타입을 파악하기
