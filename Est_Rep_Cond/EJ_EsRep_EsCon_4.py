# Leer 10 números y mostrar solamente los números positivos, y su sumatoria.
# Ej 4

sum_pos = 0

for i in range(10):
    numero = float(input('Ingrese un número: '))
    if numero > 0:
        print(numero)
        sum_pos += numero
        
print('La suma de números positivos es; ', sum_pos)