import re

bom_map = {
    'feff': 'utf-16-be',
    'fffe': 'utf-16-le',
    'efbbbf': 'utf-8-sig'
}
encodings = ['utf-8', 'utf-16-le', 'utf-16-be', 'latin-1']
words = []
patterns = None
for line in open('input.txt', encoding='utf-8'):
    line = line.strip()
    if line == '':
        patterns = []
        continue
    if patterns is None:
        bom = re.findall(r'feff|fffe|efbbbf', line)
        if len(bom) > 0 and bom[0] in bom_map:
            x = bytes.fromhex(re.sub(r'feff|fffe|efbbbf', '', line)).decode(bom_map[bom[0]])
            if '\x00' not in x and x.islower():
                words.append(x)
        else:
            for encoding in encodings:
                try:
                    x = bytes.fromhex(re.sub(r'feff|fffe|efbbbf','', line)).decode(encoding)
                    if '\x00' not in x and x.islower():
                        words.append(x)
                except Exception:
                    pass
    else: patterns.append(line)

out = 0
for pattern in patterns:
    c = pattern.replace('.', '')
    match = [x for x in words if re.match(rf'^{pattern}$', x, re.IGNORECASE)]
    out += words.index(match[0]) + 1
print(out)
