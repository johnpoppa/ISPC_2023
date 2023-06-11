# Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo
# el cambio de dólares a pesos y que sea el usuario quién decida qué tipo
# de cambio quiere, si de dólares a pesos o viceversa.
# Ej 5

cambio = input('Ingrese el tipo de cambio que desea realizar (pe para pesos a dólares, do para dólares a pesos ): ')

if cambio == "pe":
    pesos = float(input('Ingrese la cantidad de pesos: '))
    cambio = 0.004
    dolares = pesos * cambio
    print(f'Usted cambio esta cantidad de ${pesos} a U$D{dolares}')
elif cambio == "do":
    dolares = float(input('Ingrese la cantidad de dolares: '))
    cambio = 244.408
    pesos = dolares * cambio
    print(f'Usted cambio esta cantidad de U$D{dolares} a ${pesos}')
else:
    print('Moneda incorrecta...')