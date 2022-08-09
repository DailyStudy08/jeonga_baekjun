import sys
a = [0]* 10
m = [0]* 10

for i in range(10):
    a[i] = int(sys.stdin.readline())
#a완성
    m[i] = a[i]%42
#m완성
d=[m[0]]
for el in m:
    if el not in d:
        d.append(el)
print(len(d))

    