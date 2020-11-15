l = int(input())
matrix = [[0 for j in range(l)] for i in range(l)]
n = 1  # start number
start_index = 0
end_index = l - 1
while start_index < end_index:
    for i in range(start_index, end_index):
        matrix[start_index][i] = n
        n += 1
    for i in range(start_index, end_index):
        matrix[i][end_index] = n
        n += 1
    for i in range(end_index, start_index, -1):
        matrix[end_index][i] = n
        n += 1
    for i in range(end_index, start_index, -1):
        matrix[i][start_index] = n
        n += 1
    start_index += 1
    end_index -= 1
if l % 2 == 1:
    matrix[start_index][end_index] = n
for i in range(l):
    for j in range(l):
        print(matrix[i][j], end=' ')
    print()