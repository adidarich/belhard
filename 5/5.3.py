#Вывести четные числа от 2 до N по 5 в строку
n = int(input('N: '))
if (n % 2) == 0:
    print('{0} is Even '.format(n))
else:
    print('{0} is Odd '.format(n))