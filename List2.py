tmp = 0
result = []
numbers = [int(i) for i in input().split()]
for i in range(0, len(numbers)):
    if i == 0:
        result.insert(i, numbers[-1] + numbers[1])
    elif i == len(numbers) - 1:
        result.insert(i, numbers[-2] + numbers[0])
    else:
        result.insert(i, numbers[i - 1] + numbers[i + 1])
print(result)