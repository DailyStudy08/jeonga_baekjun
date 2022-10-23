n = int(input())
arr = list(map(int, input().split()))
x = int(input())
cnt = 0
arr.sort()
l, r = 0, n-1

while l != r:
    if arr[l] + arr[r] == x:
        cnt += 1
        l += 1
    elif arr[l] + arr[r] > x:
        r -= 1
    elif arr[l] + arr[r] < x:
        l += 1
print(cnt)