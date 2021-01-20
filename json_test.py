import json
from collections import defaultdict

read_data = json.loads(input())
tmp_dict = {}
in_data = defaultdict(list)
list_keys = []


# Input data transform in convenient type
for elem_of_list in read_data:
    tmp_dict[elem_of_list['name']] = elem_of_list['parents']

for key, values in tmp_dict.items():
    list_keys.append(key)
    for value in values:
        in_data[value].append(key)
list_keys.sort()


def sons_count(parent, in_dict):
    visited, stack = set(), [parent]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(set(in_dict[vertex]) - visited)
    return f'{parent} : {len(visited)}'


for elem in list_keys:
    print(sons_count(elem, in_data))