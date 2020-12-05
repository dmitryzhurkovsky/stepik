n, k = map(int, input().split())


def combination_count(n, k):
    if k > n:
        return 0
    elif k == 0:
        return 1
    else:
        return combination_count(n - 1, k) + combination_count(n - 1, k - 1)


print(combination_count(n, k))
