while True:
    s = input()
    if s == '.':
        break

    stk = []

    for i in s:
        if i == '(' or i == '[':
            stk.append(i)
        elif i == ')':
            if len(stk)!=0 and stk[-1] == '(':
                stk.pop()
            else:
                stk.append(')')
                break
        elif i == ']':
            if len(stk)!=0 and stk[-1] == '[':
                stk.pop()
            else:
                stk.append(']')
                break

    if len(stk) == 0:
        print('yes')
    else:
        print('no')