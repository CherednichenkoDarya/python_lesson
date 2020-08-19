"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""
def my_func(num_1 = 0, num_2 = 0, num_3 = 0):
    while True:
        num_1 = input("Введите число ")
        if num_1.isdigit():
            num_1 = int(num_1)
            break
        print("Некорректное число ")
    while True:
        num_2 = input("Введите число ")
        if num_2.isdigit():
            num_2 = int(num_2)
            break
        print("Некорректное число ")
    while True:
        num_3 = input("Введите число ")
        if num_3.isdigit():
            num_3 = int(num_3)
            break
        print("Некорректное число ")
    min_num = min(num_1, num_2, num_2)
    min_num = int(min_num)
    sum_num = num_1 + num_2 + num_3 - min_num
    return print(sum_num)

my_func(num_1 =0 , num_2 =0, num_3=0)