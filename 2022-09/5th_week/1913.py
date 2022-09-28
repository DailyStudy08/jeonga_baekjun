import sys
input = sys.stdin.readline

dr = [1,0,-1,0]
dc = [0,1,0,-1]

N = int(input().rstrip())
find_int = int(input().rstrip())
board=[[0]*N for _ in range(N)]
number = N*N
r,c = 0, 0
d_idx = 0
center= N //2
while True:
    if number==1:
        break
    board[r][c] = number
    nr, nc = r + dr[d_idx], c + dc[d_idx]
    if 0<= nr <N and 0 <= nc <N and board[nr][nc]==0:
        r, c = nr, nc
        number -= 1
    else:
        d_idx = (d_idx+1) % 4

board[center][center] = 1
for i in range(N):
    print(*board[i])
for i in range(N):
    for j in range(N):
        if board[i][j] == find_int:
            a = [i+1, j+1]
print(*a)

'''
1 ) NameError 의 의미
'''