N, M = map(int, input().split())
arr = [list(input())for _ in range(N)]

# 정보는 N행 M열

# 맨 왼쪽이 흰색인 경우: 짝수행은 check_w, 홀수행은 check_b
check_w = ['W','B'] * 4
check_b = ['B', 'W'] * 4
# arr에 틀을 이동시킨다. 틀 안에 check_w와 check_b 가 있는지 확인
# 다시 칠해야하는 정사각형의 최소개수는 일치하는 정사각형이 최대인 틀에서 발생
# goal: 일치하는 정사각형이 제일 많은 경우를 찾고 그 일치수를 찾는다.

maxV = 0
for i in range(N-8+1):
    for j in range(M-8+1):
        # 틀 안의 8 X 8 과 패턴이 일치하는지
        cnt1 = 0
        cnt2 = 0
        for p in range(8):
            for q in range(8):
                # 8 x 8에 대해 모두 세기 그러니까 break 는 없고,
                # 틀의 시작 첫번쨰 원소가 B라면, bwbwbwbw에서 일치하는 cnt1, wbwbwbwb에서 일치하는 cnt2를 따로 구한다.
                if arr[i][j] == 'B':
                    if p%2:
                        if (arr[i+p][j+q] == check_w[q]):
                            cnt1 += 1
                    else:
                        if arr[i+p][j+q] == check_b[q]:
                            cnt1 += 1
                    if p%2:
                        if arr[i+p][j+q] == check_b[q]:
                            cnt2 += 1
                    else:
                        if arr[i+p][j+q] == check_w[q]:
                            cnt2 += 1

                # 틀의 첫 원소가 'w'라면
                else:
                    if p%2:
                        if arr[i+p][j+q] == check_b[q]:
                            cnt1 += 1
                    else:
                        if arr[i+p][j+q] == check_w[q]:
                            cnt1 += 1

                    if p%2:
                        if (arr[i+p][j+q] == check_w[q]):
                            cnt2 += 1
                    else:
                        if arr[i+p][j+q] == check_b[q]:
                            cnt2 += 1
        # cnt1, cnt2 완성
        if maxV < cnt1:
            maxV = cnt1
        if maxV < cnt2:
            maxV = cnt2

# maxV완성
print(64-maxV)




# 맨 왼쪽이 검은색인 경우: