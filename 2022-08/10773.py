K = int(input())
stack = []

for _ in range(K):
    a = int(input())
    if a !=0:
        stack.append(a)
    else:
        stack.pop()
print(sum(stack))