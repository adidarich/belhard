#Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами
text = "Tools are any objects other"
example = "-".join(text.split(' '))
print(example)
print(text.replace(' ', '-'))


#example = text.split(' ')
#text = "-".join(example)
#print(text)


