#Пользователь вводит 3 числа, сказать сколько из них положительных
#и сколько отрицательных
a: int = int(input('Enter first number: '))
b: int = int(input('Enter second number: '))
c: int = int(input('Enter third number: '))

pos_number = (a > 0) + (b > 0) + (c > 0)
neg_number = (a < 0) + (b < 0) + (c < 0)
zero_number = (a == 0) + (b == 0) + (c == 0)
print(f'{pos_number=}')
print(f'{neg_number=}')
print(f'{zero_number=}')



