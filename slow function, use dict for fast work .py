n = int(input())
cashe = {}
for i in range(n):
    x = int(input())
    if x not in cashe:
        cashe[x] = f(x)
    print(cashe[x])

