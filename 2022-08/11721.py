s = input()
while True:
    if len(s) == 0:
        break
    print(s[:10])
    s = s[10:]