import bcrypt
from unicodedata import normalize

logins = {}
attempts = None
for line in open('test.txt', encoding='utf-8'):
    line = line.strip()
    if line == '':
        attempts = {}
        continue

    username, password = line.split()
    if attempts is None:
        logins[username] = {
            'hash': password,
            'salt': password[:29]
        }
    else:
        if username not in attempts:
            attempts[username] = []
        attempts[username].append(password)

valid = 0
for k, v in attempts.items():
    hash, salt = logins[k].values()
    print(k, hash)
    for password in v:
        new_hash = bcrypt.hashpw(normalize('NFC', password).encode('utf-8'), salt.encode('utf-8')).decode()
        print(k, new_hash)
        if hash == new_hash:
            valid += 1
print(valid)
