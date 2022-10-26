from collections import deque

delta = [[1,0], [-1,0], [0,1], [0,-1]]

def bfs(data):
    que = deque([])
    for i in range(R):
        for j in range(C):
            if data[i][j]==1:
                que.append((i, j))
    while que:
        r, c = que.popleft()
        for d in range(4):
            nr, nc = r + delta[d][0], c + delta[d][1]
            if 0<= nr< R and 0<= nc < C and data[nr][nc]==0:
                data[nr][nc] = data[r][c] + 1
                que.append((nr, nc))


C, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
maxV = 0
bfs(board)
for el in board:
    for x in el:
        if x==0:
            print(-1)
            exit(0)
    temp = max(el)
    if maxV < temp:
        maxV = temp

print(maxV -1)

