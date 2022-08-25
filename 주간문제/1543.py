book = input()
ptn = input()
cnt = 0
i = 0
while i < len(book)- len(ptn)+1:
    #검사
    length = 0
    for j in range(len(ptn)):
        if book[i] == ptn[j]:
            length += 1
            if length == len(ptn):
                i += 1
                cnt += 1
                break
            i += 1
            continue
        else:
            i = i - (length-1)
            # 되돌아가야한다. 왜냐하면 틀을 하나씩 이동하는 것이기 때문에
            break
print(cnt)
