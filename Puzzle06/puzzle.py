import re

words = []
patterns = []
switch = False
for line in open('input.txt', encoding='utf-8'):
    line = line.strip()
    if line == '':
        switch = True
        continue
    if not switch:
        if (len(words) + 1) % 3 == 0:
            line = line.encode('iso-8859-1').decode('utf-8')
        if (len(words) + 1) % 5 == 0:
            line = line.encode('iso-8859-1').decode('utf-8')
        words.append(line)
    else: patterns.append(line)

out = 0
for pattern in patterns:
    c = pattern.replace('.', '')
    match = [x for x in words if re.match(rf'^{pattern}$', x, re.IGNORECASE)]
    out += words.index(match[0]) + 1
print(out)
