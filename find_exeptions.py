from collections import deque
exeptions_tree = {}
searched = set()
searched_queue = deque()

n = int(input())
for i in range(n):
    son, *parents = input().replace(':', ' ').split()
    exeptions_tree[son] = parents

def is_parents(son, searched_queue): # почему если удалить деку, то будет ошибка. но множество searched и printed не добавляются
    searched_queue.clear()
    searched.add(son)
    searched_queue += exeptions_tree[son]
    while searched_queue:
        node = searched_queue.popleft()
        if node in searched:
            return True
        else:
            searched_queue += exeptions_tree[node]
    return False

printed = set()
m = int(input())
for i in range(m):
    son = input()
    if is_parents(son, searched_queue) is True and son not in printed:
        print(son)
        printed.add(son)
