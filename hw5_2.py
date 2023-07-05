# Создайте функцию генератор чисел Фибоначчи
def f(n):
    x, y = 0, 1
    for i in range(1, n):
        x, y = y, (x + y)
        yield x
print(*(f(9)))
