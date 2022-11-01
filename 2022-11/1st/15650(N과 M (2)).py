import sys
sys.stdin = open('input.txt', 'r')

def solution(num):
    if len(s)==M:
        print(' '.join(map(str,s)))
        return
    for i in range(num, N+1):
        if i not in s:
            s.append(i)
            solution(i+1)
            s.pop()

            
N,M = map(int, input().split())
s = []
solution(1)



