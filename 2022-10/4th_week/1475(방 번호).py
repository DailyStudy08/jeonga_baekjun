cnt = [0]*10
plate = input()
for i in range(len(plate)):
    num = int(plate[i])
    if num==6 or num==9:
        if cnt[6]==cnt[9]:
            cnt[6]+=1
        else:
            cnt[9]+=1
    else:
        cnt[num] += 1

maxV = 0
for j in range(10):
    if cnt[j]>maxV:
        maxV = cnt[j]
print(maxV)