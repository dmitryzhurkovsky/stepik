def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    else:
        key = key * 2
        if key in d:
            d[key].append(value)
        else:
            d[key] = [value]