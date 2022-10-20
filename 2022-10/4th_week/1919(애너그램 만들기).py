def a_count(word):
    alp = 'abcdefghijklmnopqrstuvwxyz'

    cnt = [0]*26
    for el in word:
        for i in range(26):
            if el ==alp[i]:
                cnt[i] += 1
    return cnt


word1 = input()
word2 = input()
word1_cnt = a_count(word1)
word2_cnt = a_count(word2)

cnt = 0
for i in range(26):
    if word1_cnt[i] != word2_cnt[i]:
        cnt += abs(word1_cnt[i]-word2_cnt[i])
print(cnt)
