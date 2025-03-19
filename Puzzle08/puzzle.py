import re
from unidecode import unidecode

out = 0
with open('./input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        valid = True
        if not (4 <= len(line) <= 12):
            valid = False
        if not re.search(r'[0-9]', line):
            valid = False
        if not re.search(r'[A-Z]', unidecode(line)):
            valid = False
        if not re.search(r'[a-z]', unidecode(line)):
            valid = False
        if not any([c for c in line if ord(c) > 127]):
            valid = False

        if valid:
            out += 1
print(out)