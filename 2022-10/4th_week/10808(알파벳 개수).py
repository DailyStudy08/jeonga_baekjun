alp = 'abcdefghijklmnopqrstuvwxyz'
word = input()
cnt = [0]*26
for el in word:
    for i in range(26):
        if el==alp[i]:
            cnt[i] += 1
print(*cnt)