def is_leap_year(year):
#判断是否闰年
    if year %4==0 and year%100!=0 or year%400==0:
        return True
    else:
        return False
def get_num_of_days_in_month(year,month):
#判断该月天数
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    elif is_leap_year(year):
        return 29
    else:
        return 28
def get_total_num_of_day(year,month):
#获取累计天数，从1800年1月1日起，周三
    days=0
    for y in range(1800, year):
        if is_leap_year(y):
            days+=366
        else:
            days+=365
    for m in range(1,month):
        days+= get_num_of_days_in_month(year,m)
    return days
def get_start_day(year,month):
#获取本月第一天周几
    return (3+get_total_num_of_day(year,month))%7
# 月份与名称对应的字典
month_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
              7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
def get_month_name(month):
    return month_dict[month]
def print_month_title(year,month):
    print("       ",  get_month_name(month),"  ",year)
    print("  ---------------------------")
    print("  Sun Mon Tue Wed Thu Fri Sat")
def print_num(year,month):
#打印日历数字部分
    d=get_start_day(year,month)
    print_month_title(year,month)
    if d!=0:
        print(' ',end='')
        print('    '*d,end='')
    for i in range(1,get_num_of_days_in_month(year,month)+1):
         print("%4d"%i,end='')
         d += 1
         if (d%7==0):
             print('')

year=int(input('年份：'))
month=int(input('月份：'))
print_num(year,month)



