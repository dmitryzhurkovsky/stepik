n = int(input())
count = 0
position = 1
for i in range(n):
    print(position, end=' ')
    count += 1
    if count == position:
        position += 1
        count = 0