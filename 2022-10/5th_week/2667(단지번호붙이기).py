import sys
sys.stdin = open('input.txt', 'r')

delta = [[0,1], [0,-1], [1,0], [-1,0]]
from collections import deque
def bfs(start):
    global cnt
    q = deque()
    i, j = start
    if check[i][j]==1:
        return
    q.append(start)
    while q:
        r, c = q.popleft()
        check[r][c]=1
        cnt += 1
        for d in range(4):
            nr, nc = r + delta[d][0], c + delta[d][1]
            if 0<=nr<N and 0<=nc<N and data[nr][nc]==1 and check[nr][nc]==0:
                check[nr][nc]=1
                q.append((nr, nc))



N = int(input())
data = [list(map(int, input())) for _ in range(N)]
check = [[0]*N for _ in range(N)]
result = []
c = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        if data[i][j]==1:
            bfs((i, j))
            if cnt:
                c += 1
                result.append(cnt)
result.sort()
print(c)
for el in result:
    print(el)




