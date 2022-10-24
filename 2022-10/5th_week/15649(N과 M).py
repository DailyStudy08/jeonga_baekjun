import sys
sys.stdin = open('input.txt', 'r')

def re():
    if len(check)==M:
        print(' '.join(map(str,check)))
        return
    for i in range(1, N + 1):
        if i not in check:
            check.append(i)
            re()
            check.pop()


N, M =map(int,input().split())
check = []
re()