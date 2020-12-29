from collections import defaultdict
data = defaultdict(list)
avarage_height = 0
with open('/Users/dmitry/Downloads/dataset_3380_5.txt', 'r') as infile, \
        open('/Users/dmitry/Downloads/outfile.txt', 'w') as outfile:
    for line in infile:
        line = line.split()
        data[int(line[0])].append(int(line[2]))

    for i in range(1, 12):
        if i in data.keys():
            for j in data[i]:
                avarage_height += j
            avarage_height = avarage_height / len(data[i])
            outfile.write(f'{i} {avarage_height}\n')
            avarage_height = 0
        else:
            outfile.write(f'{i} -\n')