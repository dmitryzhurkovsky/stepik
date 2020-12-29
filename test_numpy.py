from numpy import *

a = array([(1, 2, 3, 4), (2, 4, 6, 7)])

print(a)
print(a.ndim) # размерность массива(вложенность)
print(a.shape) # число столбцов, строк
print(a.size) # общее количество элементов

z = zeros((2,8))
print(z)
print()

s = arange(10, 59, 5)
print(s)
print()

a = linspace(0, 2, 15)
print(a)

j =  arange(24).reshape(2, 3, 4)

print(j)