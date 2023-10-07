"""Создайте функцию генератор чисел Фибоначчи fibonacci"""


def fibonacci(num):
    ZERO = 0
    prev = ZERO
    current = 1
    if num == 0:
        yield None
        return
    yield ZERO
    if num == 1:
        return
    yield current
    for _ in range(2, num):
        prev, current = current, current + prev
        yield current


for i, num in enumerate(fibonacci(0), start=1):
    print(num)
