import re
from unidecode import unidecode

def recurring_letters(string):
    string = unidecode(string).lower()
    for c in set(string):
        if string.count(c) > 1:
            return True
    return False

out = 0
with open('./input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        valid = True
        if not (4 <= len(line) <= 12):
            valid = False
        if not re.search(r'[0-9]', line):
            valid = False
        if not re.search(r'[aeiou]', unidecode(line), re.IGNORECASE):
            valid = False
        if not re.search(r'[bcdfghjklmnpqrstvwxyz]', unidecode(line), re.IGNORECASE):
            valid = False
        if recurring_letters(line):
            valid = False

        if valid:
            out += 1
print(out)