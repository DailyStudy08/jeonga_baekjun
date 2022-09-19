# def trans_to(number):
#     lstV = list(number)
#     sumV = 0
#     for i in range(0, len(number),2):
#         sumV = number[i]*3
#     for i in range(1, len(number)-1,2):
#         sumV = number[i]
#
#     if sumV % 10==0:
#         return
#     else:
#         return -1
#
# def finder_start(a_input, N):
#     for i in range(N-1,0,-1):
#         if a_input[i] == '1':
#             return i
#     else:
#         return
# # a = input()
# # print(a[3:4])
#
# N, M = map(int, input().split())
# arr = [0]*56
# for j in range(N):
#     a = input()
#     # 여기가 아님!
#     if finder_start(a, M):
#         c = j, finder_start(a, M)
#
#         arr = a[c-56:c+1]
#         print(arr)
# number_str = ''
# # for i in range(0,56,7):
#     # number_str += pw_dict[arr[i:i+7]]
# print(number_str)
#
#
# def find_end(N, M):
#     for i in range(N):
#         for j in range(M-1,55-1,-1):
#             if arr[i][j]=='1':
#                 return i, j-55
# num={'0001101':0,
#          '0011001':1,
#          '0010011':2,
#          '0111101':3,
#          '0100011':4,
#          '0110001':5,
#          '0101111':6,
#          '0111011':7,
#          '0110111':8,
#          '0001011':9
#          }
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int,input().split())
#     arr = [input() for _ in range(N)]
#     # end = M
#     # for i in range(N):
#     #     for j in range(M-1,55-1,-1):
#     #         if arr[i][j]=='1':
#     #             end = j
#     #             break
#     #     if end != M:
#     #         break
#     si, sj = find_end(N, M)
#     code = [0]*8
#     for i in range(8):
#         code[i] =num[arr[si][sj:sj+7]]
#         sj += 7
#
#     check = (code[0]+code[2]+code[4]+code[6])*3 + (code[1]+code[3]+code[5]+code[7])
#     ans =0
#     if check%10==0:
#         ans = sum(code)
#     print(f'#{tc} {ans}')
#
#
#
# def f(n,m,t):
#     for i in range(n):
#         for j in range(m-1,54,-1):
#             if t[i][j]==1:
#                 pwd = [0]*8
#                 for k in range(7,-1,-1):
#
#
#
#
# for i in range(N):
#     for j in range(N):
#         for k in range(1,N+N+2):
#             cnt = 0
#             '''
#             for p,q in home: # this way
#             '''
#             for p in range(N):
#                 for q in range(N):
#                     if city[p][q]:
#                         dis = abs(i-p)+abs(j-q)
#                         if dis < k:
#                             cnt += 1
#             if M*cnt >= cost[k]:
#                 if maxV < cnt:
#                     maxV = cnt
import math

T = int(input())
for _ in range(T):
    a = input()
    b = int(math.sqrt(len(a)))
    result = ''
    for i in range(b-1,-1,-1):
        for j in range(0, len(a),b):
            word = a[j:j+b]
            result += word[i]
    print(result)