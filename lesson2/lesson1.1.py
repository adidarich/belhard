# Напишите программу, которая запрашивает с ввода восемь чисел, добавляет их в список.
# На экран выводит их сумму, максимальное и минимальное из них. Для нахождения суммы,
# максимума и минимума воспользуйтесь встроенными в Python функциями sum(), max() и min().

lst = []

for x in range(0, 8):
    count = int(input('>>> '))
    x += 1
    lst.append(x)
    print(sum(lst))
    #print(max(lst))
    #print(min(lst))
print(lst)


# i = 0
# lst = []
#
# while i < 8:
#     count = int(input('>>>: '))
#     i += 1
#     lst.append(count)
#     print(max(lst))
# print(lst)
