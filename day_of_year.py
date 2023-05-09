def is_year_leap(year):
    is_leap_year = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_leap_year = True
        else:
            is_leap_year = True
    return is_leap_year

def days_in_month(year, month):
    days = None
    days_31 = [1, 3, 5, 7, 8, 10, 12]
    days_30 = [4, 6, 9, 11]

    if month in days_31:
        days = 31
    if month in days_30:
        days = 30

    if month == 2:
        if is_year_leap(year):
            days = 29
        else:
            days = 28
    
    return days

def day_of_year(year, month, day):
    
    days = day
    for i in range(month - 1):
        days += days_in_month(year, i + 1)
    
    return days

print(day_of_year(2000, 12, 31))
print(day_of_year(2005, 1, 30))
print(day_of_year(2000, 6, 22))
print(day_of_year(2021, 5, 23))
