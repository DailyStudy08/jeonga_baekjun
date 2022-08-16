import sys
from collections import deque
N = int(sys.stdin.readline())
q = deque([])

for _ in range(N):
    s = sys.stdin.readline().split()
    order = s[0]
    if order == 'push':
        q.append(s[1])
    elif order == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif order == 'size':
        print(len(q))
    elif order == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif order == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])

    # 시간초과가 나는 이유: que의 구조상..
