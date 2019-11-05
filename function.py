#from year entered, checks for divisibilty and returned as True/False
def is_leap(year):
    return year % 4 == 0 and (
    year % 400 == 0 or
    year % 100 != 0)
#enter year(1990) into integer form
year = int(input())
#prints True/False if it's a leap year.
print(is_leap(year))
