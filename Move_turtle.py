x, y = 0, 0


def turple_move(direction: str, move):
    global x, y
    if direction == 'север':
        y += int(move)

    if direction == 'юг':
        y -= int(move)

    if direction == 'восток':
        x += int(move)

    if direction == 'запад':
        x -= int(move)


move_count = int(input())
for i in range(move_count):
    turple_move(*input().split())
print(x, y)