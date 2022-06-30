#Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами
text_exp = "Tools are any objects other"
example = text_exp.split(' ')
text_exp = "-".join(example)
print(text_exp)

book = "Digital computers based on manipulating discrete binary digits"
print(book.replace(' ', '-'))

