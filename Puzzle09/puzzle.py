from datetime import datetime

people = {}
for line in open('input.txt'):
    date, names = line.strip().split(': ')
    for name in names.split(', '):
        if name not in people:
            people[name] = []
        people[name].append(date)

formats = ['%y-%m-%d', '%y-%d-%m', '%d-%m-%y', '%m-%d-%y']
names = []
for k, v in people.items():
    for f in formats:
        try:
            dates = [str(datetime.strptime(date, f).date()) for date in v]
        except ValueError:
            continue

        if '2001-09-11' in dates:
            names.append(k)

print(*sorted(names))
