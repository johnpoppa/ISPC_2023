# Introducir los lados de un triángulo y visualizar por pantalla si dicho
# triángulo es equilátero, isósceles o escaleno.
# Ej 1

lado1 = float(input('Ingrese el primer lado: '))
lado2 = float(input('Ingrese el segundo lado: '))
lado3 = float(input('Ingrese el tercer lado: '))

if lado1 == lado2 == lado3:
    print('Es un trinagulo Equilatero ')
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print('Es un triangulo Escaleno ')
else: 
    print('El triangulo es Isóceles')
