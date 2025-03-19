cost = 0
for line in open('input.txt', encoding='utf-8'):
    line = line.strip()
    twit_valid = len(line) <= 140
    sms_valid = len(line.encode()) <= 160

    if twit_valid and sms_valid:
        cost += 13
    elif sms_valid:
        cost += 11
    elif twit_valid:
        cost += 7

print(cost)
