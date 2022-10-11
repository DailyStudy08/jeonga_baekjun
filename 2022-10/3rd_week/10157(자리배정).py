
d = [[1,0], [0, 1], [-1, 0], [0,-1]]
C, R = map(int, input().split())
N = int(input())

board = [[0]*(C) for _ in range(R)]
r,c = 0, 0
board[r][c] = 1
number = 2
idx = 0
ans =[]
while True:
    if number==C*R+1:
        break
    nr, nc = r + d[idx%4][0], c+ d[idx%4][1]
    if 0<=nr<R and 0<=nc<C and board[nr][nc]==0:
        board[nr][nc]= number
        if number == N:
            ans.append((nc + 1,nr+1))
            break
        r, c = nr, nc
        number += 1
    else:
        idx += 1
for i in range(R):
    for j in range(C):
        if board[i][j]==N:
            ans.append((j+1, i+1))
if N > R*C:
    print(0)
else:
    ###########################질문1 출력구현?
    print(f'{ans[0][0]} {ans[0][1]}')
