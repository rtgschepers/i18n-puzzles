from dateutil import parser
import pytz

dates = []
with open('./input.txt', 'r') as file:
    for line in file:
        date = parser.parse(line.strip()).astimezone(pytz.utc)
        date = date.replace(second=0)
        dates.append(date)

for date in set(dates):
    if dates.count(date) >= 4:
        print(str(date).replace(' ', 'T'))