N = int(input())
data=[list(map(int, input().split())) for _ in range(N)]

board = [[0]*100 for _ in range(100)]

def coloring(x,y):
    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] += 1

for i in range(N):
    coloring(data[i][0],data[i][1])
    for p in range(100):
        for q in range(100):
            if board[p][q] == 2:
                board[p][q] -= 1
    # 작업 완료

    sumV = 0
for i in range(100):
    for j in range(100):
        sumV += board[i][j]
print(sumV)