import sys
sys.stdin = open('input.txt','r')

def all_blue(data, n,r,c):
    sumV = 0
    for i in range(n):
        for j in range(n):
            sumV += data[r+i][c+j]
    if sumV == n**2:
        return True
    else:
        return False

def all_white(data, n,r,c):
    sumV = 0
    for i in range(n):
        for j in range(n):
            sumV += data[r+i][c+j]
    if sumV == 0:
        return True
    else:
        return False


def quadra(data,n,i,j):
    global cnt1, cnt2
    if n==1:
        if data[i][j] ==1:
            cnt2 += 1
        else:
            cnt1 += 1
        return
    if all_blue(data,n,i,j):
        cnt2 += 1
        return
    if all_white(data,n,i,j):
        cnt1 += 1
        return
    else:
        next = n//2
        quadra(data,next,i,j)
        quadra(data,next,i+next,j)
        quadra(data,next,i,j+next)
        quadra(data,next,i+next,j+next)




    pass

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt1 = cnt2 = 0
quadra(arr,N,0,0)
print(cnt1)
print(cnt2)
