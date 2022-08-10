import sys

T = int(input())
a = [0] * T
for _ in range(T):
    a[_] = sys.stdin.readline()
for el in a:
    for i in range(len(el)):
        if el[i] == 'O':
            