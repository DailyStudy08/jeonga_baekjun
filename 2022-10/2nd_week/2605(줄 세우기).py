import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
data= list(input().split())
result = []
for i in range(N):
    result.insert(i-eval(data[i]),str(i+1))
print(' '.join(list(result)))