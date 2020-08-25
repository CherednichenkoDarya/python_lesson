"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
 количества слов в каждой строке
"""
fname = input('Файл: ')
f = open(fname,'w')
while True:
    s = input()
    if s == '': break
    f.write(s+'\n')
f.close()
f = open(fname)
line = 0
for i in f:
    line += 1

    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(i, len(i), 'симв.', word, 'сл.')

print(line, 'стр.')
f.close()