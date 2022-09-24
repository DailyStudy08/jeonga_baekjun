import sys
sys.stdin = open('input.txt', 'r')

N =input()
number_lenth =len(N)
number = int(N)
result = number

if number_lenth == 3:
    result = 99
    for num in range(100, number+1):
        n0, n1, n2 = num//100, (num%100)//10, (num%100)%10
        if n0-n1 == n1-n2:
            result += 1
elif number_lenth == 4:
    result = 144
print(result)

