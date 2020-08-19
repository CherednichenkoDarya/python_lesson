"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой.
"""
def user (name, surname, year, city, email, tel):
    return print("Здраствуйте ",name, surname, "Вам ", year, "лет", "Ваш город ", city, "Ваши контакты ", email, tel)

# Просим у пользователя данные
name = input("Введите имя ")
surname = input("Введите фамилию ")
# Проверяем год рождения
while True:
    year = input("Введите год рождения ")
    if year.isdigit():
        year = int(year)
        break
    print("Некорректный год рождения ")
city = input(" Введите город проживания ")
email = input("Введите email ")
while True:
    tel = input("Введите телефон ")
    if tel.isdigit():
        tel = int(tel)
        break
    print("Некорректный телефон ")

user(name, surname, year, city, email, tel)

