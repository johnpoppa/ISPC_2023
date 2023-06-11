# Leer 10 números y obtener la cantidad de mayores y la cantidad de
# menores a 100, cuál es el número máximo y cuál es el número mínimo.
# Ej 2

nros = []

for i in range(10):
    num = int(input('Ingrese los números: '))
    nros.append(num)
    
cant_may = 0
cant_men = 0

num_max = float('-inf')
num_men = float('inf')

for num in nros:
    if num > 100:
        cant_may += 1
    elif num < 100:
        cant_men += 1
        
    if num > num_max:
        num_max = num
        
    if num < num_men:
        num_men = num
        
print('Cantidad de números mayores al 100 es: ', cant_may)
print('Cantidad de números menores al 100 es: ', cant_men)
print('Numero máximo: ', num_max)
print('Número menor: ', num_men)
        