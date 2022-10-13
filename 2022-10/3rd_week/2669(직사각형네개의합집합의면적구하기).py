board=[[0]*101 for _ in range(101)]
for _ in range(4):
    x1,y1,x2,y2= map(int, input().split())
    for j in range(x1, x2):
        for i in range(y1, y2):
            board[i][j] = 1
sumV = 0
for row in board:
    sumV += sum(row)
print(sumV)