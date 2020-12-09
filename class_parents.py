from collections import deque
search_queue = deque()
graph = {}

class_count = int(input())
for i in range(class_count):
    son, *parents = input().replace(':', ' ').split()
    if son not in graph:
        graph[son] = parents


def node_is_parents(parents, son, search_queue):
    search_queue.clear()
    searched = set()
    if parents == son:
        return True
    search_queue += graph[son]
    while search_queue:
        node = search_queue.popleft()
        if parents == node:
            return True
        else:
            if node not in searched:
                search_queue += graph[node]
                searched.add(node)
    return False


requerments_count = int(input())
for i in range(requerments_count):
    parents, son = input().split()
    if node_is_parents(parents, son, search_queue) is True:
        print('Yes')
    else:
        print('No')



