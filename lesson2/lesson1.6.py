names: str = input('Напишите свое имя >>> ')

names = names.capitalize()

verify = ['Banana', 'Peach', 'Apple', 'Juice', 'Grape', 'Cherry']

for name in verify:
    if names == name:
        print(f'Приветствую дорогой мой друг {names}')
        break
else:
    print('ТУТ НИЧЕГО НЕТ! ЕСТЬ ЕЩЕ ВОПРОСЫ?')
