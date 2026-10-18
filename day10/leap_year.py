def is_leap_year(year):
    if year%4 == 0:
        if year % 100 == 0: 
            if year % 400 == 0:
                return True
            return False
        True
    return False

def print_leap_year_result(year):
    print(f"Is {year} a leap year? {is_leap_year(year)}")

print_leap_year_result(2000)
print_leap_year_result(2100)
print_leap_year_result(2400)
print_leap_year_result(1989)
print_leap_year_result(2020)
