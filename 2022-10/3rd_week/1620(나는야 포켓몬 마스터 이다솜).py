import sys

N, M = map(int, input().split())
# pkmon_lst = [0]*(N+1)
# for i in range(1, N+1):
#     pkmon_lst[i] = input()
# for j in range(M):
#     q = sys.stdin.readline().strip()
#     if q.isnumeric():
#         print(pkmon_lst[int(q)])
#     else:
#         for i in range(1,N+1):
#             if q == pkmon_lst[i]:
#                 print(i)

pkdict={}
arr=[]
for i in range(1, N+1):
    s = sys.stdin.readline().rstrip()
    pkdict[s]= i
    arr.append(s)
for j in range(M):
    q = sys.stdin.readline().rstrip()
    if q.isnumeric():
        print(arr[int(q)-1])
    else:
        print(pkdict[q])