# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

dictionary = {0: input('name: '),
              1: input('email: ')

}
name = {i: 'name' for i in range(1, 11)}
email = {a: 'email' for a in range(1, 11)}

print(name, email)