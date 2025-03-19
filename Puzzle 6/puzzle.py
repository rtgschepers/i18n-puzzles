out = x = y = 0
lines = [list(x[:-1]) for x in open('input.txt').readlines()]

while y < len(lines)-1:
    x, y = x + 2, y + 1
    line = lines[y]
    if line[x % len(lines[0])] == '💩':
        out += 1
print(out)