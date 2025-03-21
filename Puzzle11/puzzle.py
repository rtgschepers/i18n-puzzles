greek_lower = 'αβγδεζηθικλμνξοπρστυφχψω'
names = ['οδυσσευσ', 'οδυσσεωσ', 'οδυσσει', 'οδυσσεα', 'οδυσσευ']

def rot_n(s, n):
    trans = str.maketrans(greek_lower, greek_lower[n:] + greek_lower[:n])
    return str.translate(s, trans)

out = 0
for line in open('input.txt', encoding='utf-8'):
    line = line.strip().lower().replace('ς', 'σ')
    for i in range(1, len(greek_lower) + 1):
        x = rot_n(line, i)
        matches = [name for name in names if name in x]
        if len(matches):
            out += i
            break
print(out)
