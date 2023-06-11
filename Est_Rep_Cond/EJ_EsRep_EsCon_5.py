# Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.
#Ej 5
num_positivos = []

for i in range(15):
    numero = float(input('Ingrese un número negativo: '))
    if numero < 0:
        numero = abs(numero)
        num_positivos.append(numero)
        
print('Números convertidos a positivos: ')
for numero in num_positivos:
    print(numero)