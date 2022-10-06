import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

delta = [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]

def bfs(x, y, cnt):
    q.append([x, y])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == spot[1][0] and y == spot[1][1]:
            return visited[x][y] -1
        for d in delta:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny]==0:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y]+1

T = int(input())
for tc in range(1, T+1):
    l = int(input())
    board = [[0]*l for _ in range(l)]
    spot = [[0]*2 for _ in range(2)]
    for i in range(2):
        spot[i][0], spot[i][1] = map(int, input().split())
    #spot의 0번은 지금 자리, 1번은 다음자리
    q = deque()
    visited=[[0]*l for _ in range(l)]
    print(bfs(spot[0][0], spot[0][1],0))

