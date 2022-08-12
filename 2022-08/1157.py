a =input()

new_a = a.upper()
N = len(new_a)
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
cntl = [0] * 26
#몇개인지 구해라

for idx in range(len(alpha)):
    cnt = 0
    for i in range(len(new_a)):
        if alpha[idx] == new_a[i]:
            cnt += 1
    cntl[idx] = cnt

max_idx= 0
for i in range(len(cntl)):
    if cntl[i]>cntl[max_idx]:
        max_idx = i
result = alpha[max_idx]
for j in range(len(cntl)):
    if j != max_idx:
        if cntl[max_idx] == cntl[j]:
            result = '?'
print(result)