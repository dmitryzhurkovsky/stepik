def f(x):
    if -2 < x <= 2:
        return - x / 2
    elif x > 2:
        return (x - 2) ** 2 + 1
    else:
        return 1 - (x + 2) ** 2