from datetime import date
from datetime import time
from datetime import datetime
import calendar

today=date.today()
print(today)
now=datetime.now()
print(now)
print(now.strftime("Today's date is %d"))
s=calendar.TextCalendar(calendar.SUNDAY)
t=s.formatmonth(2020,9)
print(t)

