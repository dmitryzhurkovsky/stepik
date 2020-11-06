s = input()
a = input()
b = input()
count = s.count(a)
if count == 0:
    print(count)
else:
    count = 0
    while a in s and count <= 1000:
        s = s.replace(a, b)
        count += 1
    if count >= 1000:
        print("Impossible")
    else:
        print(count)
