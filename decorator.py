from datetime import datetime


def count_time(func_in):

    """This function counts execution time input function"""

    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func_in(*args, **kwargs)
        print(datetime.now() - start)
        return result

    return wrapper




# @count_time
def create_list_for(n):
    list = []
    for i in range(n ** 4):
        list.append(i)

    return list


# @count_time
def create_list_comprehension(n):
    list = [i for i in range(n ** 4)]

    return list


n = 10

# create_list_for(10)
# create_list_comprehension(10)

########################################################################################################################


def lower_text(func_in):

    def wrapper(string):
        result = func_in(string.lower())
        return result

    return wrapper


def upper_text(func_in):

    def wrapper(string):
        result = func_in(string.upper())
        return result

    return wrapper


@lower_text
def print_word(x):
    """ sadsdsaads"""
    print(x)


x = "Michel"
# print(help(print_word))

# print_word(x)

########################################################################################################################


def counter_calls(func_in):

    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func_in(*args, **kwargs)
        print("Функция", func_in.__name__, "была вызвана", wrapper.count, "раз.", end=' ')
        print()
        return result

    wrapper.count = 0
    return wrapper


# @counter_calls
# @count_time
def print_word2(x):
    print(x)

# print_word2('asa')
# print_word2('terra')

########################################################################################################################


def counter():
    count = 0

    def wrapper():
        nonlocal count
        count += 1
        return count

    return wrapper
