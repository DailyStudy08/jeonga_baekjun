N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
max_idx = max_h = max_h_idx = -1
for i in range(N):
    if max_idx < arr[i][0]:
        max_idx = arr[i][0]
    if max_h < arr[i][1]:
        max_h = arr[i][1]
        max_h_idx = arr[i][0]
# print(max_idx, max_h, max_h_idx)
# print(arr)
bottom = [0]*(max_idx + 1)
for i in range(N):
    bottom[arr[i][0]]=arr[i][1]
# print(bottom)
sumV = 0
temp = 0
for i in range(max_h_idx+1):
    if bottom[i]>temp:
        temp = bottom[i]
    sumV += temp
temp = 0
for i in range(max_idx, max_h_idx, -1):
    if bottom[i]>temp:
        temp = bottom[i]
    sumV += temp
print(sumV)
