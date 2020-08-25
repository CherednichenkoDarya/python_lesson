"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
дохода сотрудников.
"""
import  math
fname = input('Файл: ')
f = open(fname,'w')
while True:
    s = input("Введите фамилию и зарплату сотрудника  ")
    if s == '': break
    f.write(s+'\n')
f.close()
f = open(fname)
len = 0
workers = {}
for line in f:
    key, value = line.split()
    workers[key] = value
    len +=1
    if int(value) < 20000:
        print(f'{key}: зарплата меньше 20000')

