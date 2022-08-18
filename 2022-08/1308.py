def search_ly(year):
    if (year%4==0 and year%100 !=0) or year%400==0:
        return True
    if year%100==0:
        return False

def count_day(year, month, day):
    d = day
    lunar_month = [0, 31,29,31,30,31,30,31,31,30,31,30]
    unlunar_month = [0, 31,28,31,30,31,30,31,31,30,31,30]
    if search_ly(year):
        for i in range(month):
            d += lunar_month[i]
    else:
        for i in range(month):
            d += unlunar_month[i]
    return d

day1 = list(map(int, input().split()))
day2 = list(map(int, input().split()))
year1 = day1[0]
year2 = day2[0]
gap_d = count_day(year2, day2[1], day2[2]) - count_day(year1, day1[1], day1[2])

if year1 == year2:
    print(f'D-{gap_d}')
else:
    for i in range(year1, year2):
        cnt =0
        if search_ly(i):
            cnt += 1
    if(gap_d + 366*cnt + 365*(year2-year1-1> 365*(1000-242)+366*(250-10+2)):
        print('gg')
    else:
        print(f'D-{gap_d + 366*cnt + 365*(year2-year1-1)}')

