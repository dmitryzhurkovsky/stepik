sum_in = 0
result = 0
while True:
    a = int(input())
    sum_in += a
    result += a ** 2
    if sum_in == 0:
        break
print(result)
