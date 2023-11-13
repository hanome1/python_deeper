"""
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple. Каждый объект хранит:
имя файла без расширения или название каталога,
расширение, если это файл,
флаг каталога,
название родительского каталога.
"""

import pathlib
from collections import namedtuple
import logging
import argparse

LOG_FORMAT = '{levelname}, {asctime}, {msg}'
logging.basicConfig(format=LOG_FORMAT, style='{', filename='log.log', encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger(__name__)


def log_dec(f):
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            logger.error(f'Ошибка {e} в функции {f.__name__} с аргументами: {args}, {kwargs}')
        return None
    return wrapper


Item = namedtuple('File', ['filename', 'ext', 'flag', 'dir_name'])


@log_dec
def dir_info(path: str) -> namedtuple:
    path = pathlib.Path(path)
    res = []
    for file in path.iterdir():
        res.append(Item(file.name.split('.')[0], file.suffix, file.is_dir(), file.parent))
    return res


def par():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--path', metavar='PATH', type=str, nargs=1, help='input the path to dir', default='E:\GB\python_deeper')
    args = parser.parse_args()
    print(args)
    print(f'В скрипт передано: {args}')
    return dir_info(args.path)


# for item in dir_info('E:\GB\python_deeper'):
#     print(item)
#     pass
# for item in dir_info('sdsr'):
#     print(item)
#     pass
print(par())