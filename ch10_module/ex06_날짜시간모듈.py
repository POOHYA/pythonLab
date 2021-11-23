#   날짜 및 시간 관련 처리 모듈
#   import datetime
#   datetime.date()
#   datetime.time()
#   datetime.datetime()


import datetime

set_day = datetime.date(2019, 3, 1)
print(set_day)

print('{0}/{1}/{2}'.format(set_day.year, set_day.month, set_day.day))

day1 = datetime.date(2021, 11, 23)
day2 = datetime.date(2022, 2, 25)
diff_day = day2 - day1
print(diff_day)

print(type(day1))

print(type(diff_day))

print(datetime.date.today())

today = datetime.date.today()
special_day = datetime.date(2021, 12, 25)
print(special_day-today)


now = datetime.datetime.now()
print(now)

print("Date & Time: {:%Y-%m-%d, %H:%M:%S}".format(now))

print("Date: {:%Y, %m, %d}".format(now))
print("Time: {:%H / %M / %S}".format(now))

set_dt = datetime.datetime(2017, 12, 1, 12, 30, 45)
print(set_dt)
print("차이: ", format(set_dt-now))
