read = True
tmp = 0
matrix = []
result = []
row = 0
col = 0
while read:
    tmp = input().split()
    if "end" in tmp:
        tmp = 0
        read = False
    else:
        matrix.append([int(i) for i in tmp])
row = len(matrix)
col = len(matrix[0])
for i in range(row):
    for j in range(col):
        for di in range(-1, 2, 2):
            ai = i + di
            if ai == row:
                tmp += matrix[0][j]
            else:
                tmp += matrix[ai][j]
        for dj in range(-1, 2, 2):
            aj = j + dj
            if aj == col:
                tmp += matrix[i][0]
            else:
                tmp += matrix[i][aj]
        result.append(tmp)
        tmp = 0
for i in range(len(result)):
    print(result[i], end=' ')
    if (i+1) % col == 0:
        print()
