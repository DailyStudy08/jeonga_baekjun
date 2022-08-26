K = int(input())
data = [list(map(int, input().split())) for _ in range(6)]

length_l = [0]*6
for i in range(6):
    length_l[i] = data[i][0]

v = 0
h = 0
for i in range(6):
    if (length_l[i%6]==length_l[(i+2)%6]) and (length_l[(i+1)%6]==length_l[(i+3)%6]):
        small = data[(i+1)%6][1] * data[(i+2)%6][1]

    if length_l[i] == 3:
        v += data[i][1]
    if length_l[i] == 1:
        h += data[i][1]
big = v * h
print(K*(big - small))