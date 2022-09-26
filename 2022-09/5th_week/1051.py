import sys
sys.stdin = open('input.txt', 'r')

def row_finder(N,M,data):
    n = N
    while True:
        for i in range(N-n+1):
            for j in range(M-n+1):
                if data[i+0][j+0]==data[i+0][j+n-1] and data[i+0][j+0]==data[i+n-1][j+0] and data[i+0][j+n-1]==data[i+n-1][j+n-1]:
                    return n
        n -= 1

def col_finder(N, M, data):
    n = M
    while True:
        for i in range(N-n+1):
            for j in range(M-n+1):
                if data[i+0][j+0]==data[i+0][j+n-1] and data[i+0][j+0]==data[i+n-1][j+0] and data[i+0][j+n-1]==data[i+n-1][j+n-1]:
                    return n
        n -= 1




N, M = map(int, input().split())
arr = list(list(map(int, input())) for _  in range(N))

if N<=M:
    print((row_finder(N, M, arr))**2)
else:
    print((col_finder(N, M, arr))**2)

