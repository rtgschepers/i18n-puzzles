import datetime

from dateutil import parser
import pytz


def determine_timezone(date):
    hal = pytz.timezone('America/Halifax')
    san = pytz.timezone('America/Santiago')
    if str(date) == str(date.astimezone(pytz.utc).astimezone(hal)):
        return hal
    return san


out = i = 0
for line in open('test.txt', encoding='utf-8'):
    i += 1
    date, c, w = line.strip().split()
    date = parser.parse(date)
    tz = determine_timezone(date)
    date = date.astimezone(pytz.utc)
    date -= datetime.timedelta(minutes=int(w))
    date += datetime.timedelta(minutes=int(c))
    out += date.astimezone(tz).hour * i
print(out)
