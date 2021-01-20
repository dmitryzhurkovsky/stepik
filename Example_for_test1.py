def hash(astring, tablesize):
    hash.sum = 0
    for pos in range(len(astring)):
        hash.sum += pos * ord(astring[pos])

    return hash.sum % tablesize


print(r'C:\file.txt')
