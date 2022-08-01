N = int(input())

lstV=[]
d = 2
while d <= N:
    if not(N % d):
        lstV.append(d)
        N = N//d
    else:
        d += 1
lstV.sort()
for el in lstV:
    print(el)
        