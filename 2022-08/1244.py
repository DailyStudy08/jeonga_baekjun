def switch(data, idx):
    if data[idx] == 1:
        data[idx] = 0
    else:
        data[idx] = 1
    return


def t1(data, num):
    for i in range(1, N+1):
        if i %num ==0:
            switch(data,i)
    return


def t2(data, num):
    switch(data, num)
    for k in range(N//2):
        if num + k > N or num - k <1:
            break
        if data[num+k] == data[num-k]:
            switch(data, num+k)
            switch(data, num-k)
        else:
            break
    return


N = int(input())
status = [2] + list(map(int, input().split()))
C = int(input())
for i in range(C):
    gender, num = map(int, input().split())
    if gender == 1:
        t1(status, num)
    elif gender == 2:
        t2(status, num)
result = status[1:]
while len(result) != 0:
    s = result[:20]
    print(' '.join(map(str,s)))
    result = result[20:]