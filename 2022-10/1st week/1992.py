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
    global result
    if n==1:
        if data[i][j] ==1:
            result += '1'
        else:
            result += '0'
        return
    if all_blue(data,n,i,j):
        result +='1'
        return
    if all_white(data,n,i,j):
        result += '0'
        return
    else:
        next = n//2
        result = result+'('
        quadra(data,next,i,j)
        quadra(data,next,i,j+next)
        quadra(data,next,i+next,j)
        quadra(data,next,i+next,j+next)
        result = result + ')'

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
result = ''
quadra(arr,N,0,0)
print(result)
