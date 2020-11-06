lst = [int(i) for i in input().split()]
result = []
x = int(input())
if x not in lst:
    print("Отсутствует")
else:
    for i in range(0, len(lst)):
        if x == lst[i]:
            print(i, end=' ')