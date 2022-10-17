import sys
sys.stdin = open('input.txt', 'r')

delta =[[0,1],[0,-1],[1,0],[-1,0]]

def bfs(start):
    q=[start]
    board[start[0]][start[1]]=-1
    cnt = 0
    while q:
        r, c = q.pop(0)
        cnt += 1
        for k in range(4):
            nr, nc = r + delta[k][0], c + delta[k][1]
            if 0<= nr<M and 0<= nc<N and board[nr][nc]==0:
                q.append((nr, nc))
                board[nr][nc]= -1
    return cnt


M, N, K = map(int, input().split())
board = [[0]*N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    s_i, s_j, r, c = y1, x1, y2-y1, x2-x1
    for i in range(s_i, s_i + r):
        for j in range(s_j, s_j + c):
            board[i][j] = 1
bfs_lst = []
for i in range(M):
    for j in range(N):
        if board[i][j]==0:
            bfs_lst.append(bfs((i,j)))
bfs_lst.sort()
print(len(bfs_lst))
print(*bfs_lst)