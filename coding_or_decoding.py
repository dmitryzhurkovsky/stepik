key_in, key_out, str_to_encrypt, str_to_decode = (input() for i in range(4))
key_encrypt = dict(zip(key_in, key_out))
key_decode = dict(zip(key_out, key_in))


def encrypt(data):
    result = []
    for symbol in data:
        result.append(key_encrypt[symbol])
    return result


def decode(data):
    result = []
    for symbol in data:
        if key_decode[symbol] == symbol:
            result.append(key_decode[symbol])
        else:
            result.append(symbol)
    return result


result_encrypt = encrypt(str_to_encrypt)
print(''.join(result_encrypt))
result_decode = decode(str_to_decode)
print(''.join(result_decode))
