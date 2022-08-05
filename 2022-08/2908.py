lstV=input().split()
num1= int(lstV[0][-1])*100 + int(lstV[0][1])*10 + int(lstV[0][0])
num2= int(lstV[1][-1])*100 + int(lstV[1][1])*10 + int(lstV[1][0])
if num1>num2:
    print(num1)
else:
    print(num2)
    