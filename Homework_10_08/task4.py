"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
 Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""
n = 1
for user_list in input("Введите несколько слов: ").split():
    print( n, ".", user_list)
    n +=1