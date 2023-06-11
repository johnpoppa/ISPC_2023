# Realice un programa que pida un número del 1 al 12 y diga el nombre
# del mes correspondiente.
#Ej 5

num = int(input('Ingrese un número del 1 al 7: '))

if num == 1:
    mes = 'Enero'
elif num == 2:
    mes = 'Febrero'
elif num == 3:
    mes = 'Marzo'
elif num == 4:
    mes = 'Abril'
elif num == 5:
    mes = 'Mayo'
elif num == 6:
    mes = 'Junio'
elif num == 7:
    mes = 'Julio'
elif num == 8:
    mes = 'Agosto'
elif num == 9:
    mes = 'Septiembre'
elif num == 10:
    mes = 'Octubre'
elif num == 11:
    mes = 'Noviembre'
elif num == 12:
    mes = 'Diciembre'
else:
    mes = 'El dato ingresado debe ser un número del 1 al 12.'

print('El número ', num, 'tiene asignado el mes', mes)