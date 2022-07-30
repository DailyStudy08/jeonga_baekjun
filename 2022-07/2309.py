import sys

mylst = [int(sys.stdin.readline().strip()) for i in range(9)]

for i in range(len(mylst)):
    for j in range(i+1, len(mylst)):
        if mylst[i]+mylst[j] == sum(mylst) - 100:
            num1 = mylst[i]
            num2 = mylst[j]
            mylst.remove(num1)
            mylst.remove(num2)
            break
mylst.sort()
for el in mylst:
    print(el)