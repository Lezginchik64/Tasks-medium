from calendar import *

year = int(input("Enter Year: "))
# print(calendar(year, 2, 1, 8, 2)) # Вывод календаря

cal = TextCalendar(firstweekday=0)  # Monday

month_num = int(input("Enter Month: "))
print(cal.formatmonth(year, month_num))
