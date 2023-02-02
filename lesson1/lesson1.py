# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами

user: str = input('Write Sentence >>> ')

print(user.replace(' ', '-'))

print('-'.join(user.split(' ')))

# userTwo: str = 'Tools are any objects other'
# example_one = userTwo.replace(' ', '-')
# example_two = '-'.join(userTwo.split(' '))
# print(example_one, '\n', example_two)
