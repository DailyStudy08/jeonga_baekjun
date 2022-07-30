T = int(input())

for i in range(T):
    num, mylst = input().split()
    num = int(num)
    mylst = list(mylst)
    mylst.pop(num - 1)
    print(''.join(mylst))