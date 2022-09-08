import sys
N = int(sys.stdin.readline())
while True:
    flag = True
    for i in str(N):
        if i != '4' and i!= '7':
            N -= 1
            flag = False
    if flag:
        print(N)
        break