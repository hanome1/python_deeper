"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions.
"""

import fractions

frac1 = fractions.Fraction(input('input first fraction: '))
frac2 = fractions.Fraction(input('input second fraction: '))
print(frac1 + frac2, frac1 * frac2, sep="\n")