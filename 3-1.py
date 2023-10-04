"""
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
[1, 2, 3, 1, 2] -> [1, 2]
"""

default_list = [1, 2, 3, 1, 2]

def has_duplicates(usr_list):
    res = set()
    for i in usr_list:
        if usr_list.count(i) > 1:
            res.add(i)
    return list(res)

def has_duplicates_1(usr_list):
    res = []
    for i in usr_list:
        if usr_list.count(i) > 1 and res.count(i) == 0:
            res.append(i)
    return res

print(default_list, has_duplicates(default_list), has_duplicates_1(default_list))