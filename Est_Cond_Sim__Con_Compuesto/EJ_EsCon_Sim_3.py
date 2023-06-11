# Realizar un programa que permita ingresar “f” o “m” y determinar si vota
# en mesa femenina o masculina.
# Ej 3


genero = input('Ingrese su genero f/m: ')
if genero == "f":
    print('Debe votar en mesa femenina')
elif genero == "m":
    print('Debe votar en mesa masculina')
else:
    print('Genero no valido...')