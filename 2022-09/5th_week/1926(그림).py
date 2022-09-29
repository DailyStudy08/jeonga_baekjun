import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
def find_one(data):
    lst =[]
    for i in range(n):
        for j in range(m):
            if data[i][j]==1:
                lst.append((i, j))
    return lst


dr = [1, -1, 0, 0]
dc = [0, 0 , 1, -1]

def bfs(v, visited):
    i, j = v
    if visited[i][j]==1:
        return 0
    q.append((i, j))
    # a = set()
    area = 1

    while q:
        r, c= q.popleft()
        visited[r][c] = 1
        # a.add((r,c))
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0<= nr<n and 0<=nc<m and board[nr][nc]==1 and visited[nr][nc]==0:
                q.append((nr,nc))
                visited[nr][nc] = 1
                area += 1
                # a.append((nr,nc))
    return area








n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*m for _  in range(n)]
max_area = 0
cnt = 0
q= deque()
for el in [(0,4)]:
    a = bfs(el,visited)
    if a:
        cnt += 1
    if a> max_area:
        max_area = a
print(cnt)
print(max_area)
