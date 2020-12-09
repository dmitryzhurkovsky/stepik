count = 1
x = input()
j = 1
i = 0
length = len(x)
while i != length:
    if i == length - 1:
        print(x[-1] + str(count), end='')
        break
    elif x[i] == x[j]:
        count += 1
    else:
        print(x[i] + str(count), end='')
        count = 1
    i = i + 1
    j = j + 1
