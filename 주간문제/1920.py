'''
N = int(input())
data = list(map(int,input().split()))
M = int(input())
num = list(map(int, input().split()))
for i in range(M):
    if num[i] in data:
        print(1)
    else:
        print(0)
# 시간 초과
'''
N = int(input())
data = set(input().split())
M = int(input())
num = list(input().split())

for el in num:
    if el in data:
        print(1)
    else:
        print(0)
# 시간 초과가 나지 않았다. set의 포함여부를 확인의 시간 복잡도는 O(1)이라고 한다...

