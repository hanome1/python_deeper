"""Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
reverse_kwargs(rev=True, acc="YES", stroka=4) -> {True: "rev", "YES": 'acc', 4: "stroka"}"""

def my_func(**kwargs):
    res = dict()
    for key, value in kwargs.items():
        res[value] = key
    return res
print(my_func(rev=True, acc="YES", stroka=4))