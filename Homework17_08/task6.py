"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также
необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
from itertools import count
from itertools import cycle
my_list=[]
for a in count(1):
    if a > 15:
        break
    else:
        my_list.append(a)
print(my_list)

x = 0
for i in cycle(my_list):
    if x > 50:
        break
    print(i, end=' ')
    x += 1
