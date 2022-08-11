import sys
n = int(sys.stdin.readline())
for i in range(n):
    strV = sys.stdin.readline()
    cnt = 0
    i = 0
    #길이 안에 있는 동안은 계속 반복
    while i <len(strV):
        cnt_i = 1
        #O가 나온다면 계속 반복한다,아니면 안한다
        while strV[i]=='O':
            cnt += cnt_i
            if strV[i] == strV[i+1]:
                cnt_i += 1
            i += 1
        i += 1
    print(cnt)