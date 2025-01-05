# a = input("enter your name ", 'thanks')
# print(a, 'thanks')
#
# age = input("Введите свой возраст (учтите, что он должен быть не больше 99): ")
# print("Спасибо! Вы ввели:", age)
#
# print("Введите свой возраст ...")
# print("Но учтите, что он должен быть не больше 99.")
# age = input("Ваш возраст: ")
# print("Спасибо! Вы ввели:", age)
#
# print("Введите свой возраст (учтите, что он должен быть не больше 99): ", end="")
# age = input()
# print(f"Спасибо! Вы ввели: {age}")
# pip install prompt_toolkit
# from prompt_toolkit import prompt
#
# age = prompt("Введите свой возраст (учтите, что он должен быть не больше 99): ")
# print(f"Спасибо! Вы ввели: {age}")
# python3 -m pip install prompt_toolkit
# # from prompt_toolkit import prompt
# # print("prompt_toolkit успешно работает!")
# pip uninstall prompt_toolkit
# pip install prompt_toolkit

# a = int(input('Sample input: '))
# print('Sample output: ', a + 1)
#
# a = int(input('x: '))
# print('2x:', a*2)
# print('1/2x:', a/2)
#
# a = int(input('Enter the length of the side of the square: '))
# print('area of a square: ', a**2)
# print('area of a square: ', a*a)
#
# a = map(int, input('Enter two numbers: ').split())
# print(sum(a))
#
# a = int(input('Введите длину прямоугольника: '))
# b = int(input('Введите ширину прямоугольника: '))
# print('Периметр: ', a*2 + b*2)
# print('Площадь: ', a*b)
#
# a = int(input('F: '))
# print('C:', ((a-32)*5)/9)
#
# a = map(int, input('Enter four numbers: ').split())
# print(sum(a)/4)
#
# a = map(int, input('enter 5 exam scores (1 to 100): ').split())
# print(max(a))
#
# n = int(input('Enter the number: '))
# print(n-1, '>', n, '<', n+1)

# a = float(input('enter the number: '))
# print(round(a, 2), end=' ')
# print(round(a, 3))

# a = input("Введите разделитель: ")
# print(1, 2, 3, 4, 5, sep=a)

# a = map(int, input("Введите три целых числа: ").split())
# print(','.join(a))

# a = input("Введите три целых числа: ").split()
# print(','.join(a))

# a = int(input("Введите граммы: "))
# print('Полученные кг: ', a // 1000)

# x = int(input('Джек купил карандашей: '))
# y = int(input('Ручек: '))
# z = int(input('Маркеров: '))
# b = 3 # цена карандаша
# a = b + 2 # цена ручки
# c = a + 3 # цена маркера
# print(x*b + y*a + z*c)

# a = int(input('Введите число от 1 до 10: '))
# b = int(input('Введите второе число: '))
# c = int(input('Введите третье число: '))
# d = max(a+b+c, a+b*c, a*b+c, a*b*c, (a+b)*c, (a+b)*c)
# print(d)

# a, b, c = map(int, input('Введите три числа от 1 до 10 через пробел: ').split())
# d = max(a+b+c, a+b*c, a*b+c, a*b*c, (a+b)*c, a*(b+c))
# print(d)

# a, b, c = map(int, input('Введите три числа от 1 до 10 через пробел: ').split())
# print(a, b, c, sep=',')
#
# a = int(input("Введите число: "))
# a += 1
# print(a)
#
# a = float(input("Enter your deposit: "))
# a *= 1.5
# print(a)

t = "Hello world!"
print(t[0:len(t):1])