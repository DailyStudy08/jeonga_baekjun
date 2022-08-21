import math

A, B ,V = map(int, input().split())

v = A -B
d = math.ceil((V-A)/v) + 1
print(d)
