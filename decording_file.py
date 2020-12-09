count = '0'
char = 'a'


outfile = open('/Users/dmitry/downloads/dataset_out.txt', 'w')
with open('/Users/dmitry/downloads/dataset_3363_2.txt', 'r') as infile:
    for line in infile:
        for i in range(len(line)):
            if line[i].isdigit():
                count += line[i]
            else:
                outfile.write(char * int(count))
                char = line[i]
                count = '0'
outfile.close()


