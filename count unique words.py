from collections import defaultdict
read_data = input().lower().split()
result = defaultdict(int)
for i in read_data:
    result[i] += 1
for key, val in result.items():
    print(key, val)
print(read_data)
print(result)
