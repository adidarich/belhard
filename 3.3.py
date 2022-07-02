#Пользователь вводит Имя, Возраст и Город, сформировать
#приветственное сообщение путем форматирования 3-мя способами
#Первый способ
userName = input('Name: ')
userAge = input('Age: ')
userCity = input('City: ')

format = f'Welcome my dear {userName}!'
print(format, '\n\n')

#Второй способ
name = "Aleksandr"
age = 20
city = "Minsk"
print("My name is %s, I am %d years old. I live in %s" % (name, age, city), '\n\n')

#Третий способ
fName = "Max"
city = "Grodno"
print('Меня зовут {}, я живу в {}'.format(fName, city))