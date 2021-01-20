import requests
import re


link1, link2 = input(), input()
start = requests.get(link1)
finish = link2
patern = r'<a href="(.{1,})">'


def parcing(url, patern):
    match = re.findall(patern, url.text)
    for url in match:
        result = requests.get(url)
        if finish in result.text:
            return True
    return False


if parcing(start, patern):
    print('Yes')
else:
    print('No')