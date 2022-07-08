# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число
x = float(input('Enter Your Number: '))
s = input('Enter Symbol: ')
y = float(input('Enter Your Number: '))

if s == '+':
    print(x + y)
elif s == '-':
    print(x - y)
elif s == '*':
    print(x * y)
elif s == '/':
    print(x / y)
    if x == 0 or y == 0 and s == '/':
        print('division by zero')
else:
    print('division by zero')

# try:
#     while True: print(eval(input(">>>")))
# except Exception as e:
#     print("You got error: ", e)

# while True:
#     print(eval(input('>>> ')))
