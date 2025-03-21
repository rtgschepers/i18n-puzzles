from dateutil import tz
from dateutil.parser import parse

out = 0
lines = open('input.txt').readlines()
for i in range(0, len(lines), 3):
    a = [word for part in lines[i].split(',') for word in part.split()][1:]
    b = [word for part in lines[i+1].split(',') for word in part.split()][1:]

    dep_date = parse(f'{a[1]}-{a[2]}-{a[3]} {a[4]} CDT', tzinfos={'CDT': tz.gettz(a[0])})
    arr_date = parse(f'{b[1]}-{b[2]}-{b[3]} {b[4]} CDT', tzinfos={'CDT': tz.gettz(b[0])})
    out += (arr_date - dep_date).seconds // 60
print(out)
