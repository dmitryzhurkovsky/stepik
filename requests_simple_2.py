import requests
import re

result = set()
patern = r"(?:<a.*href=['\"])(?:.+?://)?(\w.+?)(?:[/:'\"])"

link_in = requests.get(input().strip('\n'))
match = re.findall(patern, link_in.text)
result = sorted(list(set(match)))
print('\n'.join(result))