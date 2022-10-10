import sys
sys.stdin = open('input.txt', 'r')
delta = [[1,0], [0, 1], [-1, 0], [0,-1]]
C, R = map(int, input().split())
N = int(input())

board = [[0]*(C) for _ in range(R)]
r,c = 0, 0
board[r][c] = 1
number = 2
while True:
    if number==C*R+1:
        break
    for d in delta:
        while True:
            nr, nc = r + d[0], c + d[1]
            if 0<=nr<R and 0<=nc<C and board[nr][nc] ==0:
                board[nr][nc] = number
                r, c = nr, nc
                number += 1
            else:
                break
flag=False
ans = []
for i in range(R):
    for j in range(C):
        if board[i][j] == N:
            ans.append(j+1)
            ans.append(i+1)
            flag=True
if flag:
    print(*ans)
else:
    print(0)
