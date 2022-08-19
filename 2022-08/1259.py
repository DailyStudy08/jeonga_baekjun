while True:
    s = input()
    if s =='0':
        break
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            print('no')
            break
    else:
        print('yes')