"""
Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""

def num_check():
    num = int(input('your num: '))
    if num > 0 and num < 10000:
        return num
    else:
        print('your num has to be positive and less than 10000\ntry again!')
        num_check()


num = num_check()

divider = 2
while divider < num:
    if num % divider == 0:
        print(num, ' is composite number')
        break
    divider += 1
else:
    print(num, ' is a prime number')

#test
