N = int(input())
mylst = []
for i in range(N):
    num = int(input())
    mylst.append(num)
mylst.sort()
for el in mylst:
    print(el)