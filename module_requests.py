import requests


def get_param(par1):
    par1 = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + par1).text
    print(par1)
    if par1[0] == 'W' and par1[1] == 'e':
        return par1
    else:
        get_param(par1)


with open('/Users/dmitry/downloads/dataset_3378_3.txt', 'r') as infile, open('/Users/dmitry/downloads/10.txt', 'w') as outfile:
    url = infile.read().strip()
    print(url)
    r = requests.get(url).text
    get_param(r)
    outfile.write(r)

