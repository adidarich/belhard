# На вход функция more_than_five(lst) получает список из целых чисел.
# Результатом работы функции должен стать новый список, в котором содержатся только те числа,
# которые больше 5 по модулю.

def more_than_five(lst):
    new_lst = []
    for i in lst:
        if i > 5:
            new_lst.append(i)
            return new_lst

print(more_than_five([54, 8, 91, 64, 7]))