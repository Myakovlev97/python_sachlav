a = int(input('Sample input: '))
print('Sample output: ', a + 1)

a = int(input('x: '))
print('2x:', a*2)
print('1/2x:', a/2)

a = int(input('Enter the length of the side of the square: '))
print('area of a square: ', a**2)
print('area of a square: ', a*a)

a = map(int, input('Enter two numbers: ').split())
print(sum(a))

a = int(input('Введите длину прямоугольника: '))
b = int(input('Введите ширину прямоугольника: '))
print('Периметр: ', a*2 + b*2)
print('Площадь: ', a*b)

a = int(input('F: '))
print('C:', ((a-32)*5)/9)

a = map(int, input('Enter four numbers: ').split())
print(sum(a)/4)

a = map(int, input('enter 5 exam scores (1 to 100): ').split())
print(max(a))

n = int(input('Enter the number: '))
print(n-1, '>', n, '<', n+1)