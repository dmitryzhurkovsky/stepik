def create(namespace, parent):
    """ Создает новое пространство с именем <namespace> внутри пространства <parent>"""
    spaces[namespace] = {'parent': parent, 'vars': []}


def add(namespace, var):
    """ Добавляет в пространство <namespace> переменную <var>"""
    if var not in spaces[namespace]['vars']:
        spaces[namespace]['vars'].append(var)


def get(namespace, var):
    """ Получить имя пространства, из которого будет взята переменная <var>
        при запросе из пространства <namespace>,
        или None, если такого пространства не существует
    """
    if var in spaces[namespace]['vars']:
        return print(namespace)
    if spaces[namespace]['parent'] is None:
        return None
    else:
        get(spaces[namespace]['parent'], var)


spaces = {
    'global': {'parent': None, 'vars': []}
}

n = int(input())
if 1 <= n <= 100:
    for i in range(n):
        request, namespace, arg = input().split()
        if request == 'create':
            create(namespace, arg)
        elif request == 'add':
            add(namespace, arg)
        elif request == 'get':
            get(namespace, arg)
