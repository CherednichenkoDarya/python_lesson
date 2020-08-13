"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
 весна, лето, осень). Напишите решения через list и через dict.
"""
while True:
    user_num = input("Введите число от 1 до 12 ")
    if user_num.isdigit():
        user_num = int(user_num)
        break
    print("Это не число!")
if user_num ==0 or user_num > 12:
    print("Такого месяца не существует")

dict_seasons = {'Winter': (1, 2, 12),
           'Sping': (3, 4, 5),
           'Summer': (6, 7, 8),
           'Autumn': (9, 10, 11)}

month = user_num
for key in dict_seasons.keys():
    if month in dict_seasons[key]:
        print(key)

list_seasons = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
month_two = month - 1
list_seasons[month_two]
if month_two ==11 or month_two ==0 or month_two ==1:
    print("Winter")
elif month_two ==2 or month_two==3 or month_two==4:
    print("Sping")
elif month_two ==5 or month_two==6 or month_two==7:
    print("Summer")
elif month_two==8 or month_two==9 or month_two ==10:
    print("Autumn")

