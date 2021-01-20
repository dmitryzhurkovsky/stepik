import itertools

def primes():
    i = 2
    deviser_count = 0
    while True:
        for deviser in range(1, i + 1):
            if i % deviser == 0:
                deviser_count += 1
        if deviser_count <= 2:
            yield i
        deviser_count = 0
        i += 1


print(list(itertools.takewhile(lambda x: x <= 31, primes())))
