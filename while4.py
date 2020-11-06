count = 1
result = []
n = int(input())
while len(result) < n:
    result.append(count)
    if result.count(count) == count:
        count += 1
    print(*result)
