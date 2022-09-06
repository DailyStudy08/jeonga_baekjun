N, M = map(int,input().split())
board = [list(input()) for _ in range(N)]

cnt_r = 0
cnt_c = 0

for i in range(N):
    if 'X' not in (board[i]):
        cnt_r += 1
for i in range(M):
    if 'X' not in ([board[j][i] for j in range(N)]):
        cnt_c += 1
print(max(cnt_r, cnt_c))