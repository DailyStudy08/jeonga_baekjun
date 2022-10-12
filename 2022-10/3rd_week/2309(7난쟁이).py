import sys
sys.stdin = open('input.txt', 'r')


def recur(cnt,sum):
    global check, flag
    if flag:
        return
    '''여기를 판단 못함'''
    if cnt == 7:
        if sum==100:
            flag=True
            for i in range(len(check)):
                if check[i]==1:
                    print(data[i])
    for i in range(9):
        if check[i]==0:
            check[i]=1
            recur(cnt +1, sum+data[i])
            check[i]=0


data = [0]*9
for i in range(9):
    data[i] = int(input())
data.sort()
check =[0]*9
flag= False
recur(0,0)