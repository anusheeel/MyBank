import datetime

x = datetime.datetime.now()
year = x.year
month = x.strftime("%b")
day_of_month = x.strftime("%d")
weekday = x.strftime("%A")

print(year,"/", month ,"-", day_of_month ,"/" ,weekday)
