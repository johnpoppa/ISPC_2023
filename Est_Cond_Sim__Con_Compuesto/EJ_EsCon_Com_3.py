# Realice un programa que lea tres números, muestre cuál es el mayor y
# determine si es par o impar.
# Ej 3

num1 = int(input('Ingrese el 1° número: '))
num2 = int(input('Ingrese el 2° número: '))
num3 = int(input('Ingrese el 3° número: '))

may = num1

if num2 > may:
    may = num2

if num3 > may:
    may = num3
    
print('El mayor es: ', may)

if may % 2 == 0:
    print('El número mayor es par...')
else:
    print('El número mayor es impar')