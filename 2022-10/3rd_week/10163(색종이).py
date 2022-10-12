import sys
sys.stdin = open('input.txt', 'r')

board=[[0]*1002 for _ in range(1002)]
N = int(input())
for k in range(1,N+1):
    c, r, w, h = map(int, input().split())
    for i in range(r, r+h):
        for j in range(c, c+w):
            board[i][j] = k

for p in range(1, N+1):
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if board[i][j]==p:
                cnt += 1
    print(cnt)