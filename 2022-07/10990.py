n = input()


for i in range(n):
    if i:
        print(' '*(n-i) +'*'+ ' '*(2*i - 1)+'*' )
    else:
        print(' '*n + '*')