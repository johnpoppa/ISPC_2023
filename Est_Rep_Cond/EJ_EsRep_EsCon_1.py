# Realice un programa que lea 4 números y diga cuántos son pares y
# cuantos impares y devuelva la sumatoria de los pares.
# Ej 1

nros = []

for i in range(4):
    num = int(input('Ingrese un número: '))
    nros.append(num)

cant_pares = 0
cant_impares = 0
suma_par = 0

for num in nros:
    if num % 2 == 0:
        cant_pares += 1
        suma_par += num
    else:
        cant_impares += 1

print('Cantidad de números pares: ', cant_pares)
print('Cantidad de números impares: ', cant_impares)
print('La suma de nros. pares es : ', suma_par)

       
        
        
