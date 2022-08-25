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
            if length==0:
                i+=1
            break
        #모두 맞아 ...아니에요
    #length 완성
print(cnt)


# 답이 자꾸 틀리네요... 어떻게 풀지 구상을 다시 해야겠어요
