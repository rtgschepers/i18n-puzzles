import re
from unidecode import unidecode


def contains_recurring(string):
    for c in set(string):
        if string.count(c) > 1:
            return True
    return False


out = 0
with open('./input.txt', encoding='utf-8') as file:
    for line in file:
        line = unidecode(line.strip()).lower()
        valid = True
        if not (4 <= len(line) <= 12):
            valid = False
        if not re.search(r'[0-9]', line):
            valid = False
        if not re.search(r'[aeiou]', line):
            valid = False
        if not re.search(r'[bcdfghjklmnpqrstvwxyz]', line):
            valid = False
        if contains_recurring(unidecode(line)):
            valid = False

        if valid:
            out += 1
print(out)
