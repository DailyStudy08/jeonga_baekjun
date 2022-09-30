def is_no_zero(data, M, N):
    for i in range(M):
        for j in range(N):
            if data[i][j] == 0:
                return False
    return True


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
M, N = map(int, input().split())
board = [[0]*N for _ in range(M)]
r = c = 0
cnt = 0
idx = 0
while True:
    if is_no_zero(board, M, N):
        break
    board[r][c] = 1
    nr, nc = r + dr[idx], c + dc[idx]
    if 0<= nr <M and 0<= nc <N and board[nr][nc]==0:
        board[nr][nc] = 1
        r, c = nr, nc
    else:
        idx = (idx + 1) % 4
        cnt += 1
print(cnt)