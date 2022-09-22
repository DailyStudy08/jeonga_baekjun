X = int(input())

x = 0
max_n = 0
while True:
    if X<= max_n:
        break
    else:
        x += 1
        max_n += x
diff = max_n - X
if x%2 == 0:
    n = x - diff
    d = diff + 1
    print(f'{n}/{d}')
else:
    n = diff + 1
    d = x - diff
    print(f'{n}/{d}')
