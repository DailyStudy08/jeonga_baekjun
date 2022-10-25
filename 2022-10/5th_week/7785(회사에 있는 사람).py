import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
a = set()
for i in range(N):
    name, record = input().split()
    if record == 'enter':
        if name not in a:
            a.add(name)
        else:
            pass
    else:
        if name not in a:
            pass
        else:
            a.remove(name)
a =list(a)
a.sort(reverse=True)
for el in a:
    print(el)