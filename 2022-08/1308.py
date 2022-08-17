def search_ly(year):
    if (year%4==0 and year%100 !=0) or year%400==0:
        return True
    if year%100==0:
        return False

def count_day(data):
    

day1 = list(map(int, input().split()))
# day1[0]
# day1[1]
# day1[2]
day2 = list(map(int, input().split()))
result = ''
if day2[0] > day1[0]:
    if day2[0]-day1[0]>1000:
        result = 'gg'
    day
