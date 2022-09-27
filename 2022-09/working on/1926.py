import sys
sys.stdin = open('input.txt','r')
dr = [1, -1, 0, 0]
dc = [0, 0 , 1, 1]

def bfs(data,v,area):
    global max_area, cnt, check
    if area>max_area:
        max_area = area
    r, c = v

    check[r][c] = 1
    for dr,dc in [[1,0],[-1,0],[0,-1],[0,1]]:
        nr, nc = r+ dr, c+dc

    return




n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
check = [[0]*m for _ in range(n)]
max_area = 0
cnt = 0
bfs(board,(0,0),0)
print(cnt)
print(max_area)