
def check_r(data):
    sumV = 0
    d = 0
    for i in range(5):
        sumV = sum(data[i])
        if sumV == 0:
            d += 1
    if d:
        return d
    else:
        return False

def check_c(data):
    d = 0
    for i in range(5):
        sumV = 0
        for j in range(5):
            sumV += data[j][i]
        # sumV 완성
        if sumV == 0:
            d += 1
    if d:
        return d
    else:
        return False


def find_change(data, val):
    for i in range(5):
        for j in range(5):
            if data[i][j] == val:
                data[i][j] = 0
    return


def check_dia1(data):
    sumV = 0
    for i in range(5):
        sumV += data[i][i]
    #sumV 완성
    if sumV == 0:
        return True
    else:
        return False

def check_dia2(data):
    sumV = 0
    for i in range(5):
        sumV += data[i][4-i]
    # sumV 완성
    if sumV == 0:
        return True
    else:
        return False




board = [list(map(int, input().split())) for _ in range(5)]
number = []
for i in range(5):
    number = number + list(map(int, input().split()))

# 답은 idx + 1
for i in range(25):
    c = 0
    find_change(board,number[i])

    if check_r(board):
        c += check_r(board)
    if check_c(board):
        c += check_c(board)
    if check_dia1(board):
        c += 1
    if check_dia2(board):
        c += 1
    if c >= 3:
        idx = i
        break
print(idx+1)