# Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 3-мя способами

name: str = str(input('Write the name >>> '))
age: int = int(input('How old are you? >>> '))
city: str = str(input('Write your city >>> '))

print(f'Welcome my dear {name}. You {age} years old and You from {city}')
print('Приветствую %s. Тебе %d лет и ты из %sa' % (name, age, city))
print('Опять ты {}. Вот твой возраст {} и город {}'.format(name, age, city))
