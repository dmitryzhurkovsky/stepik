with open('dataset_24465_4.txt', 'r') as infile, open('dataset_24465_4-in_data.txt', 'w') as outfile:
    infile = infile.read().splitlines()
    result = '\n'.join(infile[::-1])
    outfile.write(result)

