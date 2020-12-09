from simplecrypt import decrypt

with open('/Users/dmitry/downloads/encrypted.bin', 'rb') as infile:
    encrypted = infile.read()
with open('/Users/dmitry/downloads/passwords.txt', 'r') as passwords:
    passwords = (i.strip() for i in passwords)
    for i in passwords:
        try:
            s = decrypt(i, encrypted)
            print(s.decode("utf-8"))
            break
        except Exception:
            continue
