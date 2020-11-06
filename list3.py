result = []
numbers = [int(i) for i in input().split()]
if len(result) == 1:
    print(result[0])
else:
    for i in range(0, len(numbers)):
        if i == 0:
            result.insert(i, numbers[-1] + numbers[1])
        elif i == len(numbers) - 1:
            result.insert(i, numbers[-2] + numbers[0])
        else:
            result.insert(i, numbers[i - 1] + numbers[i + 1])
    for i in range(0, len(result)):
        print(result[i], end=' ')
