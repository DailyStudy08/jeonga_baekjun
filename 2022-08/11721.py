# 10 자리씩 끊어 출력하기
# 1 - 슬라이싱 이용하기
s = input()
while True:
    if len(s) == 0:
        break
    print(s[:10])
    s = s[10:]

# 2 - 인덱스에 모듈러스 연산을 사용한 반복문을 이용하기기
s = input()

for i in range(len(s)):
    print(s[i],end='')
    if (i%10 ==9):
        print()

'''
두 경우에 있어서, 사용하는 메모리나 연산시간은 같다고 하네요
'''