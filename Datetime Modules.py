import datetime

"""d = datetime.date(1994, 3, 15)
print(d)

tday = datetime.date.today()
print(tday)
print(tday.year)
print(tday.day)

print(tday.weekday())          # Monday is 0, while sunday is 6
print(tday.isoweekday())       # Monday is 1, while sunday is 7"""






"""# Timedeltas is simply the dy/dx btw two dates or times!!!


#DATES........
tday = datetime.date.today()

tdelta = datetime.timedelta(days=7)
# print(tday + tdelta)
# print(tday - tdelta)


#date2 = date1 + timedelta
#timedelta = date1 + date2

bday = datetime.date(2022, 3, 15)
till_bday = bday - tday
print(till_bday)
print(till_bday.total_seconds())"""



"""#TIME.......
t = datetime.time(8, 30, 25, 10010)
print(t)
print(t.hour)
print(t.second)"""




"""# DATE AND TIME......
dt = datetime.datetime(2022, 3, 6, 8, 59, 30, 100000)

# print(dt)
# print(dt.date())
# print(dt.time())
# print(dt.year)

# tdelta = datetime.timedelta(hours=7)
# print(dt + tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)"""





# TIMEZONES.......

import datetime
import pytz

# dt = datetime.datetime(2022, 3, 6, 7, 10, 30, 45, tzinfo=pytz.UTC)
# print(dt)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('Africa/Lagos'))
print(dt_mtn)


for tz in pytz.all_timezones:
    print(tz)

