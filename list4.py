result = []
numbers = [int(i) for i in input().split()]
numbers.sort()
tmp = numbers[0]
for i in range(1, len(numbers)):
    if tmp == numbers[i]:
        if tmp not in result:
            result.insert(i, tmp)
    tmp = numbers[i]
for i in range(0, len(result)):
    print(result[i], end=' ')