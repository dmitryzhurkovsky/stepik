import os

# path = input('Укажите необходимый путь\n')
path = '/Users/dmitry/downloads'


def iterating_over_files(path, level=1):
    print('Level =', level, 'Content:', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '/' + i):
            print('Спускаемся', path + '/' + i)
            iterating_over_files(path + '/' + i, level + 1)
            print('Возвращаемся в', path)


iterating_over_files(path)

print()
