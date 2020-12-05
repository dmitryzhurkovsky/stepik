from decorator import count_time

from collections import defaultdict
result = defaultdict(int)

tmp_value = 0


@count_time
def words_count():

    with open('/Users/dmitry/downloads/vlastelin_kolec_bratstvo_kol_ca.txt', 'r') as infile:
        for line in infile:
            cache = (i for i in line.lower().split())
            for i in cache:
                result[i] += 1
    tmp_value = 0
    tmp_key = ''
    for key, value in result.items():
        if tmp_value < value:
            tmp_value = value
            tmp_key = key
            if tmp_value == value:
                tmp_key = max(tmp_key, key)
                tmp_value = result[tmp_key]
    with open('/Users/dmitry/downloads/1.txt', 'w') as outfie:
        outfie.write(tmp_key + ' ' + str(tmp_value))


words_count()

@count_time
def a():
    s, d, m, w = str(), dict(), 0, str()
    with open('/Users/dmitry/downloads/vlastelin_kolec_bratstvo_kol_ca.txt', "r") as f:
        s = f.read().lower().strip().split()
    s.sort()
    for word in s:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    for word in d:
        if d[word] > m:
            m = d[word]
            w = word


a()