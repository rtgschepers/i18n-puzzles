from dateutil import parser
from datetime import datetime

dates = []
with open('./test.txt', 'r') as file:
    for line in file:
        line = line.strip()
        tz =
        date = datetime.strptime(line, '%Y-%m-%dT%H:%M:%S-04:00').date()