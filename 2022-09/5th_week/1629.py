import sys
sys.stdin = open('input.txt','r')

def multiple(num1,num2):
    if num2 == 1:
        return num1%c
    temp = multiple(num1, num2//2)
    if num2%2:
        return temp*temp*num1%c
    else:
        return temp*temp%c

a, b, c = map(int, input().split())
print(multiple(a,b))
