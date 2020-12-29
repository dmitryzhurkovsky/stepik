import requests

with open('/Users/dmitry/downloads/dataset_3378_2.txt', 'r') as infile:
    url = infile.read().strip()
    text = requests.get(url).text.splitlines()
    print(len(text))