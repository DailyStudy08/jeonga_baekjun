colors = ['black','brown', 'red','orange','yellow','green', 'blue','violet', 'grey', 'white']
import sys

first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()
third = sys.stdin.readline().strip()
for i in range(10):
    if colors[i]==first:
        first_i = i
    if colors[i] == second:
        second_i = i
    if colors[i] == third:
         third_i = i
print((first_i*10+second_i)*(10**third_i))
'''
딕셔너리 이용하면, 사용할 피연산자가 정해져있으면 딕셔너리에서 꺼내쓰는게 연산의 시간이 훨씬 덜 걸림
'''
colors = {
    'black': [0,1],
    'brown': [1, 10],
    'red':[2, 100],
    'orange':[3, 1000],
    'yellow':[4,10000],
    'green': [5, 100000],
    'blue':[6, 1000000],
    'violet':[7, 10000000],
    'grey':[8,100000000],
    'white':[9,1000000000]
}

first = input()
second = input()
third = input()

print((colors[first][0]*10+colors[second][0])*colors[third][1])