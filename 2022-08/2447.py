import sys
N= int(sys.stdin.readline())

def star(N):
    if N==3:
        return ['***','* *','***']
    else: 
        lstV = [0]*N
        d = N//3
        b =' ' * d
        c=star(N//3)
        for i in range(N): 
            if i < d:
                lstV[i] = c[i]*3
            elif i < (2*d):
                lstV[i] = c[i-d] + b + c[i-d] 
            else:
                lstV[i] = c[i-2*d]*3
        return lstV
print('\n'.join(star(N)))

# 시간 초과를 해결하기
#  1. input이 필요할 때, sys.stdin을 이용하기
#  2. 불필요한 반복문을 줄이기
#  3. 재사용성이 높은 계산 후 값들을 변수로 지정해 재사용하기
#  4. 리스트의 str element를 한 줄씩 print 하고싶을 때, 반복문을 이용하지 말고 join 함수를 이용하기. 자료형을 빠뜨리지 않기!
#  5. PyPy3가 Python3보다 빠를 때가 있다... 어떤 차이일까? JIT 컴파일 방식을 도입해, 복잡한 코드 특히 반복을 사용하는 경우에 우세할때가 있다고 한다.
#  6. 멋지십니다.. join 까지 
