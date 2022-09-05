x = set()
y = set()
pointV=set()
for _ in range(3):
    a, b = map(int,input().split())
    pointV.add((a,b))
    x.add(a)
    y.add(b)
for el1 in x:
    for el2 in y:
       if  (el1, el2) not in pointV:
           print(el1,el2)