import sys
sys.stdin = open('input.txt', 'r')


dr = [1,-1,0,0]
dc = [0,0,-1,1]

def bfs(r,c,cnt):
    if r == N-1 and c == M-1:
        return cnt
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0<= nr< N and 0<=nc<N and visited[nr][nc]==0 and arr[nr][nc]==1:
            visited[nr][nc] = 1
            bfs(nr,nc, cnt+1)
            visited[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
for row in arr:
    print(row)
visited =[[0]*(M) for _ in range(N)]
visited[0][0]=1
print(bfs(0, 0, 0))