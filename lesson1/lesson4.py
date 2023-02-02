# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных

num1: int = int(input('Enter the first number >>> '))
num2: int = int(input('Enter the second number >>> '))
num3: int = int(input('Enter the third number >>> '))

positive_n = (num1 > 0) + (num2 > 0) + (num3 > 0)
negative_n = (num1 < 0) + (num2 < 0) + (num3 < 0)

print(f'Positive numbers = {positive_n}; Negative numbers = {negative_n}')
