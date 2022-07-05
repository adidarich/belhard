# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

words: str = str(input('You Write a Word: '))
dictionary = {}
for i in words:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1
print(dictionary.items())