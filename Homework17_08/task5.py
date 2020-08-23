"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from random import randint
from functools import reduce

my_list = []
for i in range(20):
    my_list.append(randint(100, 1001))
sum_all = reduce(lambda x, y: x + y, my_list)

print(sum_all)