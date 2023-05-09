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



test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
