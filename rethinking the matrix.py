matrix = []
while True:
    tmp = [i for i in input().split()]
    if tmp == ["end"]:
        break
    matrix.append(tmp)
row, col = len(matrix), len(matrix[0])
for i in range(row):
    for j in range(col):
        left = int(matrix[i][j-1])
        right = int(matrix[i][j+1-col])
        up = int(matrix[i-1][j])
        bottom = int(matrix[i+1-row][j])
        result = left + right + up + bottom
        print(result, end=' ')
    print()
