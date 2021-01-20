import csv
from collections import defaultdict
tmp = 0

in_data = defaultdict(int)
with open('/Users/dmitry/Downloads/Crimes.csv', 'r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        if '2015' in row[2]:
            in_data[row[5]] += 1
    for key, value in in_data.items():
        if tmpc <= value:
            tmp = value
            result_key = key

print(in_data)
print(result_key)


from collections import Counter


with open('/Users/dmitry/Downloads/Crimes.csv') as f:
    data = csv.reader(f)
    print(Counter(row[5] for row in data if '2015' in row[2]))